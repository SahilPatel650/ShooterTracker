import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])
from time import sleep
from camera_continuity.CameraNode import CameraNode
from frame_split import split_video

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

                             

if __name__ == "__main__":
    init_cameras()
    print(monitored_cameras[0].get_video_feed(0))
    split_video.split(monitored_cameras[0].get_video_feed(0), monitored_cameras[0].get_frame_path())

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


