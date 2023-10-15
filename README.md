# ShooterTracker

## Inspiration

  

There is an alarming increase in active shooter situations around the nation, especially in colleges. Having a system that can improve safety on campus would increase our peace of mind.

  

Current warning systems have a latency of 5-10 minutes between an active shooter threat being called in and warnings being sent out to students and notifications to police departments. In most cases, police officers are sent into buildings blind, unaware of the whereabouts of a shooter. We aim to give precise location data and reduce the time it takes before students and police are aware of a threat.

  

## What it does

  

STAMP-AI takes in CCTV footage and is able to do the following:

- Detecting Guns & People

- Locating Active Shooter Threats Within A CCTV Network, Providing a live Map

- Provide an Automated Description of the Threat

  

## How we built it

  

We split STAMP-AI into submodules that all came together to create the final product and its features.

  

**Person Detection**: The person detection model is based on Ultralytics Yolo V8 which is trained on the COCO (Common Objects in Context) dataset. It is able to draw a bounding box around any people in the frame.

  

**Gun Detection**: The gun detection uses a fine tuned model that also runs on Yolo. It is trained on 1,500 custom images of guns in order to accurately detect them in a given image. This module generates a bounding box around any gun in a given frame using Darknet and OpenCV to complete the image processing. The model is able to differentiate between different types of guns (pistols, ARs, etc.).

  

**Shooter Identification**:  This module uses the location of the gun and location of all people to figure out who the active threat is. 

**AI Generated Description**: Uses the BLIP.VQA natural language model to accurately take an image of the shooter based on the shooter identificaiton bounding boxes and return a general description. This description includes shirt color, ethnicity, hat color, etc.

**Camera Continuity**: Allows STAMP to understand the relationship between cameras and visualize each camera on a map. Each camera is assigned "neighbors" that are adjacent and are searched when a gun goes out of frame.

**Core Camera Tracking**: Incorporates searching logic to tell STAMP which direction the shooter must be moving based on the last camera the gun was detected in. Allows STAMP to automatically switch cameras.
  
**Video Splice/Merge**: Splits the CCTV footage into frames which are fed into the  identification algorythms to identify the gun and shooter. This module then merges the split-up frames into a streamable video.



  

## Challenges we ran into

  

-   Library Compatibility Issues
    
-   Lack of weapon images to train a new model on YoloV8
    
-   Issues combining modules
    
-   Rendering videos frame by frame consumes a substantial amount of processing power and was slow
    
-   Tracking the shooter across multiple camera feeds and translating that to programming logic
    

  

## Accomplishments that we're proud of

-   We have provided a working base AI model to use CCTV live footage and detect and track a shooter
    
-   We used data from multiple sources and created a cohesive working algorithm to analyze the movement of the shooter
    
-   We created a live tracking map that is based off the CCTV live footage
    
-   We created multiple sub-modules with specialized purposes and combined them into one product
    

  

## What we learned

-   Fine tuning an object detection model
    
-   Using natural language models
    
-   Importance of prompt engineering when working with Large Language Models
    
-   Working in a software team with specific roles using branching and git
    
-   Splitting up a big picture into multiple smaller workflows and assigning roles
    

  

## What's next for STAMP-AI

-   Better fine tuning of gun detection model
    
-   Scalability across n number of cameras

-   Run object detection models on multiple devices, perhaps GPUs
    

-   Feature: given a picture of a building’s floor plan with CCTV cameras marked, generates a directed graph of the CCTV cameras
    
-   Notifications to police departments and students
*Detailed instructions on which direction people should be moving in with AI generated exit plans
    

-   Automatic locking of doors to confine shooter if they are alone
    *Using object detection to check if nobody else is in the room with the shooter


