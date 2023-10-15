import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
from time import sleep
from camera_continuity.CameraNode import CameraNode
from frame_split import split_video
from frame_split import merge_video

from fire_and_gun_detection import gun_detection
from person_detection import detect_person
from person_detection import id_shooter
from shooter_description import desc

#create the node of the cameras to monitor, initially all of them

NUM_CAMERAS = 4
num_frames = [0, 0, 0, 0]
monitored_cameras = []
last_detected_camera: CameraNode = None
all_cameras = []
frame = 0

def init_cameras():
    camera_1 = CameraNode(1, [1,2])
    camera_2 = CameraNode(2, [1,2,3])
    camera_3 = CameraNode(3, [2,3,4])
    camera_4 = CameraNode(4, [3,4])

    monitored_cameras.append(camera_1) 
    monitored_cameras.append(camera_2) 
    monitored_cameras.append(camera_3) 
    monitored_cameras.append(camera_4) 

    all_cameras.append(camera_1) 
    all_cameras.append(camera_2) 
    all_cameras.append(camera_3) 
    all_cameras.append(camera_4) 
    
    

def init_models():
    gun_model = gun_detection.load_yolo()
    people_model = detect_person.init_model()
    desc_model = desc.initialize_model()
    return gun_model, people_model, desc_model

if __name__ == "__main__":
    init_cameras()

    gun_model, people_model, (processor, vqa_model) = init_models()
    description = ""
    for camera_idx in range(len(all_cameras)):
        num_frames[camera_idx] = split_video.split(all_cameras[camera_idx].get_video_feed(), all_cameras[camera_idx].get_frame_path())
    common_frames = min(num_frames)

    for i in range(common_frames):
        new_monitored_cameras = []
        for camera_idx in range(len(monitored_cameras)):

            boxes, confs, class_ids = monitored_cameras[camera_idx].get_gun_bboxes(i, gun_model)
            people_boxes = monitored_cameras[camera_idx].get_people_bboxes(i, people_model)

            if len(boxes) > 0 :
                new_monitored_cameras = [monitored_cameras[camera_idx]]
                last_detected_camera = all_cameras[camera_idx]
                

            if len(people_boxes) == 0 or len(boxes) == 0:
                continue
            #add code to draw people boxes
            shooter_id = id_shooter.id_shooter(people_boxes, boxes[0])
            rendered_frame_path = monitored_cameras[camera_idx].get_rendered_frames()+"/frame"+str(i)+".jpg"
            shooter_box = people_boxes[shooter_id][:4]
            shooter_box = list(map(lambda x: int(x*0.4), shooter_box))
            gun_detection.draw_person_box(shooter_box, rendered_frame_path)
            if not description:
                description = desc.get_description(rendered_frame_path, shooter_box[:2], shooter_box[2:4], processor, vqa_model)
            print(description)


        if new_monitored_cameras == []:
            if last_detected_camera == None:
                new_monitored_cameras = all_cameras.copy()
            else:
                neighbors = last_detected_camera.get_neighbors()
                for neighbor in neighbors:
                    new_monitored_cameras.append(all_cameras[neighbor-1])


        monitored_cameras = new_monitored_cameras

            
        
        # merge frames into video
    for camera_idx in range(len(all_cameras)):
        merge_video.frames_to_video(all_cameras[camera_idx].get_rendered_frames(), 
                                    all_cameras[camera_idx].get_render_video_path(), 
                                    800,
                                    all_cameras[camera_idx])

    # while True:
    #     flagged_cameras = []
    #     for camera in monitored_cameras:
    #         print(camera.get_video_feed(frame))
    #         # implement gun detection here
    #         is_gun_detected = False
    #         if is_gun_detected:
    #             flagged_cameras.append(camera)
        
    #     sleep(1)
    #     frame += 1
