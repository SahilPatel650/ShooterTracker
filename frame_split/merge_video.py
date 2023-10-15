import cv2
import os

def frames_to_video(folder_path, output_file, common_frames, camera):
    # Get list of image files in folder and sort them

    #if a frame is missing, get it from the frame foler
    if camera != None:
        for i in range(common_frames):
            if not os.path.isfile(folder_path + "/frame" + str(i) + ".jpg"):
                print("here")
                os.system("cp " + camera.get_frame(i) + " " + camera.get_rendered_frames())

    image_files = [f for f in os.listdir(folder_path) if not f.startswith('.')]     

    # the images are stored as frame#, so sort by frame number
    image_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    # print(image_files)
    
    # Set frame rate and size of output video
    fps = 30
    img = cv2.imread(os.path.join(folder_path, image_files[0]))
    height, width, _ = img.shape
    size = (width, height)

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_file, fourcc, fps, size)

    # Loop through all image files and add them to output video
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        print(img_path)
        img = cv2.imread(img_path)        
        img_resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        video_writer.write(img_resized)

    # Release VideoWriter object
    video_writer.release()
