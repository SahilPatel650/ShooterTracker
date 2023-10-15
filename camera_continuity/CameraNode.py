import sys, os
sys.path.extend([f'./{name}' for name in os.listdir("../") if os.path.isdir(name)])
from fire_and_gun_detection import gun_detection
from person_detection import detect_person

class CameraNode:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbor(self):
        return self.neighbors
    
    def get_video_feed(self):
        #return path to directory containing video feed
        return "video-data/raw-video/camera" + str(self.value) + ".mp4"
   
    def get_frame_path(self):
        return "video-data/frames/camera" + str(self.value)
        
    def get_frame(self, frame):
        #return path to directory containing video feed
        return self.get_frame_path() + "/frame" + str(frame) + ".jpg"

    def get_rendered_frames(self):
        #return path to directory containing video feed
        return "video-data/rendered-frames/camera" + str(self.value)
    
    def get_render_video_path(self):
        return "video-data/rendered-video/camera" + str(self.value) + ".mp4"
    
    def get_gun_bboxes(self, frame, loaded_model):
        frame_path = self.get_frame(frame)
        return gun_detection.image_detect(frame_path, loaded_model)
    
    def get_people_bboxes(self, frame, model):
        frame_path = self.get_frame(frame)
        return detect_person.inference(model, frame_path)
