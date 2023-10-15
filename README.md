# ShooterTracker

## Inspiration

There is an alarming increase in active shooter situations around the nation, especially in colleges. Having a system that can improve safety on campus would increase our peace of mind. 

Current warning systems inherently include a buffer of 5-10 minutes between an active shooter threat being called in and warnings being sent out to students and notifications to police departments. In most cases, police officers are sent into buildings, blind and unaware of the whereabouts of a shooter. We aim to give precise location data along with reducing the time it takes before students and police are aware of a threat.

## What it does

STAMP-AI takes in CCTV footage and is able to do the following:
- Detecting Guns & People
- Locating Active Shooter Threats Within A CCTV Network, Providing a live Map
- Providing an Automated Description of the Threat

## How we built it

We split STAMP-AI into submodules that all came together to create the final product and its features.

**Person Detection**: The person detection dataset was based on Ultralytics Yolo V8 which is trained on the COCO (Common Objects in Context) dataset. Given a frame from a video, this module is able to draw a bounding box around any people in the frame. 

**Gun Detection**: The gun detection dataset is a custom-trained dataset that also runs on Yolo. It was trained on 1,500 custom images of guns in order to accurately detect them in a given image. This module generates a bounding box around any gun in a given frame. This module also used Darknet and OpenCV to complete the image processing.

**Shooter Identification**: Tells STAMP which person in a frame is holding the gun and then label that person as an active threat. This was done by computing the centers of the bounding boxes of the people and guns in a frame. Whichever person bounding-box center was closest to the gun bounding-box center was then labeled as the threat.

**Camera Continuity**: Allows STAMP to understand the relationship between cameras and visualize each camera on a map. Each camera is assigned "neighbors" that are adjacent and are searched when a gun goes out of frame.  

**Video Splice/Merge**: Splits the inputted CCTV footage into frames which are then inputted into the Shooter Identification module to identify the shooter. This module also has a merge function which puts all of the split-up frames back together into a viewable video.

**AI Generated Description**: Uses the BLIP.VQA natural language model to accurately take an image of the shooter and return a general description. This description includes shirt color, ethnicity, hat color, etc.

**Core Camera Tracking**: Incorporates searching logic to tell STAMP which direction the shooter must be moving based on the last camera the gun was detected in. Allows STAMP to automatically switch cameras.

## Challenges we ran into

- Library Compatibility Issues
- Lack of weapon images to train a new model on YoloV8 
- Issues combining modules
- Rendering videos frame by frame consumes a substantial amount of processing power and was slow
- Tracking the shooter across multiple camera feeds and translating that to programming logic

## Accomplishments that we're proud of
- We have provided a working base AI model to use CCTV live footage and detect and track a shooter
- We used data from multiple sources and created a cohesive working algorithm to analyze the movement of the shooter
- We created a live tracking map that is based off the CCTV live footage
- We created multiple sub-modules with specialized purposes and combined them into one product

## What we learned
- Fine tuning an object detection model
- Using natural language models
- Importance of prompt engineering when working with Large Language Models
- Working in a software team with specific roles using branching and git
- Splitting up a big picture into multiple smaller workflows and assigning roles

## What's next for STAMP-AI
- Better fine tuning of gun detection model
- Scalability across n number of cameras
- Run object detection models on multiple devices, perhaps GPUs
- Feature: given a picture of a building’s floor plan with CCTV cameras marked, generates a directed graph of the CCTV cameras
- Notifications to police departments and students
- Detailed instructions on which direction people should be moving in with AI generated exit plans
- Automatic locking of doors to confine shooter if they are alone
- Using object detection to check if nobody else is in the room with the shooter

## Usage
1. Clone the repository
2. Install OpenCV, transformers and ultralytics for python
3. Download `yolov3.weights` from [here](https://onedrive.live.com/?authkey=%21AGDaftEjlDj9k6o&id=E9C1B3533D4253D%213525&cid=0E9C1B3533D4253D&parId=root&parQt=sharedby&o=OneUp), and place it in the folder `fire_and_gun_detection`
4. Create a directory `video-data`, and directories `frames`, `raw-video`, `rendered-frames`, `rendered-maps`, `rendered-video`
5. Run `entrypoint.py`
