import os
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
        return "camera-continuity/camera" + str(self.value) + "/frame" + str(frame) + ".jpg"
