import math

def calculate_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points (x1, y1) and (x2, y2).
    
    Parameters:
    x1 (float): x-coordinate of the first point.
    y1 (float): y-coordinate of the first point.
    x2 (float): x-coordinate of the second point.
    y2 (float): y-coordinate of the second point.
    
    Returns:
    float: Distance between the two points.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_bounding_box_center(x, y, width, height):
    """
    Calculates the center coordinates of a bounding box given the top left 
    coordinates (x, y), width, and height.
    
    Parameters:
    x (float): x-coordinate of the top left corner of the bounding box.
    y (float): y-coordinate of the top left corner of the bounding box.
    width (float): Width of the bounding box.
    height (float): Height of the bounding box.
    
    Returns:
    tuple: (center_x, center_y) - center coordinates of the bounding box.
    """
    center_x = x + width / 2
    center_y = y + height / 2
    return center_x, center_y

