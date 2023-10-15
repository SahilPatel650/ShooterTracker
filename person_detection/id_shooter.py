def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

#Perform person and gun detection
def get_person_gun_distance(person_box, gun_box):
    person_midpoint = (person_box[0], person_box[1])
    gun_midpoint = (gun_box[0] + gun_box[2] / 2, gun_box[1] + gun_box[3] / 2)
    distance = calculate_distance(person_midpoint, gun_midpoint)
    return distance

def id_shooter(person_boxes, gun_box):
    distances_with_indices = [(i, get_person_gun_distance(person_boxes[i], gun_box)) for i in range(len(person_boxes))]
    return min(distances_with_indices, key=lambda x:x[1])[0]
