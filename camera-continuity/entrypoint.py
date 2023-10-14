from time import sleep
from CameraNode import CameraNode

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

    monitored_cameras.append(camera_a, 
                             camera_b, 
                             camera_c, 
                             camera_d, 
                             camera_e)


if __name__ == "__main__":
    init_cameras()
    while True:
        flagged_cameras = []
        for camera in cameras:
            print(camera.get_video_feed(frame))
            # implement gun detection here
            is_gun_detected = False
            if is_gun_detected:
                flagged_cameras.append(camera)
        


        sleep(1)
        frame += 1


