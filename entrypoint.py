import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
from time import sleep
from camera_continuity.CameraNode import CameraNode
from frame_split import split_video
from frame_split import merge_video

from fire_and_gun_detection import gun_detection
from person_detection import detect_person

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
    return gun_model, people_model

if __name__ == "__main__":
    init_cameras()
    gun_model, people_model = init_models()
    for camera_idx in range(len(monitored_cameras)):
        split_video.split(monitored_cameras[camera_idx].get_video_feed(), monitored_cameras[camera_idx].get_frame_path())
        for i in range(80, 268):
            boxes, confs, class_ids = monitored_cameras[camera_idx].get_gun_bboxes(i, gun_model)
            people_boxes = monitored_cameras[camera_idx].get_people_bboxes(i, people_model)
            # logic for shooter id goes here
            print(boxes)
            print(people_boxes)
        
        #merge frames into video
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
