class CameraNode:
    def __init__(self, value, neighbors=[]):
        self.value = value
        self.neighbors = neighbors

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def get_neighbor(self):
        return self.neighbors
    
    def get_video_feed(self, frame):
        #return path to directory containing video feed
        return "video-data/raw-video/camera" + str(self.value) + ".mp4"
    
    def get_frame(self, frame):
        #return path to directory containing video feed
        return "video-data/frames/camera" + str(self.value) + "/frame" + str(frame) + ".jpg"
    def get_rendered_frames(self):
        #return path to directory containing video feed
        return "video-data/rendered-frames/camera" + str(self.value)
    
    def get_render_video_path(self):
        return "video-data/rendered-video/camera" + str(self.value) + ".mp4"
            
