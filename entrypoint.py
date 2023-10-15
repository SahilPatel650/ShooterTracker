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

NUM_CAMERAS = 5
monitored_cameras = []
frame = 0

def init_cameras():
    camera_a = CameraNode(1)
    # camera_b = CameraNode(2)
    # camera_c = CameraNode(3)
    # camera_d = CameraNode(4)
    # camera_e = CameraNode(5)

    monitored_cameras.append(camera_a) 
    # monitored_cameras.append(camera_b) 
    # monitored_cameras.append(camera_c) 
    # monitored_cameras.append(camera_d) 
    # monitored_cameras.append(camera_e) 

def init_models():
    gun_model = gun_detection.load_yolo()
    people_model = detect_person.init_model()
    desc_model = desc.initialize_model()
    return gun_model, people_model, desc_model

if __name__ == "__main__":
    init_cameras()
    gun_model, people_model, (processor, vqa_model) = init_models()
    description = ""
    for camera_idx in range(len(monitored_cameras)):
        num_frames = split_video.split(monitored_cameras[camera_idx].get_video_feed(), monitored_cameras[camera_idx].get_frame_path())
        for i in range(num_frames):
            boxes, confs, class_ids = monitored_cameras[camera_idx].get_gun_bboxes(i, gun_model)
            people_boxes = monitored_cameras[camera_idx].get_people_bboxes(i, people_model)
            if len(boxes) == 0 or len(people_boxes) == 0:
                continue
            shooter_id = id_shooter.id_shooter(people_boxes, boxes[0])
            rendered_frame_path = monitored_cameras[camera_idx].get_rendered_frames()+"/frame"+str(i)+".jpg"
            shooter_box = people_boxes[shooter_id][:4]
            shooter_box = list(map(lambda x: int(x*0.4), shooter_box))
            gun_detection.draw_person_box(shooter_box, rendered_frame_path)
            if not description:
                description = desc.get_description(rendered_frame_path, shooter_box[:2], shooter_box[2:4], processor, vqa_model)
            print(description)
        
        # merge frames into video
        merge_video.frames_to_video(monitored_cameras[camera_idx].get_rendered_frames(), monitored_cameras[camera_idx].get_render_video_path())

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
