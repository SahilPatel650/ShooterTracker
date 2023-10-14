from time import sleep
from CameraNode import CameraNode

#create the node of the cameras to monitor, initially all of them

NUM_CAMERAS = 5
cameras = []
frame = 0



def init_cameras():
    for i in range(NUM_CAMERAS):
        cameras.append(CameraNode(i))




if __name__ == "__main__":
    init_cameras()
    while True:
        flagged_cameras = []
        for camera in cameras:
            # implement gun detection here
            print(camera.get_video_feed(frame))
        sleep(1)
        frame += 1


