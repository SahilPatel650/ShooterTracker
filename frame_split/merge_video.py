import cv2
import os

def frames_to_video(folder_path, output_file):
    # Get list of image files in folder and sort them
    image_files = os.listdir(folder_path)
    #image_files.sort()

    # the images are stored as frame#, so sort by frame number
    image_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    
    print("image_files: ", image_files)






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
        img = cv2.imread(img_path)
        video_writer.write(img)

    # Release VideoWriter object
    video_writer.release()
