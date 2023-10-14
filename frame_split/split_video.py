import cv2

def split(video_path, output_path):
    capture = cv2.VideoCapture(video_path)
    frameNum = 0
    success = True
    while success:
        success, frame = capture.read()
        if success:
            print('Read a new frame: ', output_path)
            cv2.imwrite(output_path + "/frame%d.jpg" % frameNum, frame)
            frameNum += 1