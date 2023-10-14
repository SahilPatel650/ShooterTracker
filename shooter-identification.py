# distance_calculation.py
import sys
sys.path.append('ShooterTracker')  # Add the parent directory to the Python path
from person-detection import person-detection
from fire-and-gun-detection import gun-detection
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Path to your image
image_path = "../images/your_image.jpg"

# Perform person and gun detection
person_boxes = person-detection.detect_person(image_path)
gun_boxes = gun-detection.detect_gun(image_path)

# Calculate distances
distances = []
for person_box in person_boxes:
    person_midpoint = (person_box[0] + person_box[2] / 2, person_box[1] + person_box[3] / 2)
    for gun_box in gun_boxes:
        gun_midpoint = (gun_box[0] + gun_box[2] / 2, gun_box[1] + gun_box[3] / 2)
        distance = calculate_distance(person_midpoint, gun_midpoint)
        distances.append(distance)

# Print distances
for i, distance in enumerate(distances):
    print(f"Person {i + 1} to Gun: {distance:.2f} pixels")
