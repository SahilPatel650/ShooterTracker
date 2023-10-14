import sys
from time import sleep

#create the node of the cameras to monitor, initially all of them

NUM_CAMERAS = 5
monitored_cameras = []
frame = 0



def init_cameras():
    camera_a = CameraNode(1)
    camera_b = CameraNode(2)
    camera_c = CameraNode(3)
    camera_d = CameraNode(4)
    camera_e = CameraNode(5)

    monitored_cameras.append(camera_a) 
    monitored_cameras.append(camera_b) 
    monitored_cameras.append(camera_c) 
    monitored_cameras.append(camera_d) 
    monitored_cameras.append(camera_e) 

                             

if __name__ == "__main__":
    init_cameras()
    while True:
        flagged_cameras = []
        for camera in monitored_cameras:
            print(camera.get_video_feed(frame))
            # implement gun detection here
            is_gun_detected = False
            if is_gun_detected:
                flagged_cameras.append(camera)
        

        sleep(1)
        frame += 1


