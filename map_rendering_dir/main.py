from PIL import Image, ImageDraw
import entrypoint


def get_picture(detectedCamera):
    if ((
            detectedCamera == entrypoint.init_cameras().camera_a) or  # checks if camera is c2 or c2 and c1, and sets as frame 2
            (entrypoint.monitored_cameras[0] == entrypoint.init_cameras().camera_a and entrypoint.monitored_cameras[
                1] == entrypoint.init_cameras().camera_b)):
        Image.open('frame 2.png')
    elif ((entrypoint.monitored_cameras[
               0] == entrypoint.init_cameras().camera_b) or  # checks if camera is c3 or c3 and c2, and sets as frame 3
          (entrypoint.monitored_cameras[0] == entrypoint.init_cameras().camera_b and entrypoint.monitored_cameras[
              1] == entrypoint.init_cameras().camera_c)):
        Image.open('frame 3.png')
    elif ((entrypoint.monitored_cameras[
               0] == entrypoint.init_cameras().camera_c) or  # checks if camera is c4 or c4 and c3, and sets as frame 4
          (entrypoint.monitored_cameras[0] == entrypoint.init_cameras().camera_c and entrypoint.monitored_cameras[
              1] == entrypoint.init_cameras().camera_d)):
        Image.open('frame 4.png')
    elif ((entrypoint.monitored_cameras[
               0] == entrypoint.init_cameras().camera_d) or  # checks if camera is c5 or c5 and c4, and sets as frame 5
          (entrypoint.monitored_cameras[0] == entrypoint.init_cameras().camera_d and entrypoint.monitored_cameras[
              1] == entrypoint.init_cameras().camera_e)):
        Image.open('frame 5.png')
    else:
        Image.open('frame 1.png')
