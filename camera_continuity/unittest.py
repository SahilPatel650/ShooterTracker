from util import calculate_distance, calculate_bounding_box_center
import math

def test_calculate_distance():
    # Test case 1: distance between (0, 0) and (3, 4)
    distance = calculate_distance(0, 0, 3, 4)
    print(distance)
    assert math.isclose(distance, 5.0, rel_tol=1e-2)

    # Test case 2: distance between (2, 2) and (2, 2) should be 0
    distance = calculate_distance(2, 2, 2, 2)
    print(distance)
    assert distance == 0.0

def test_calculate_bounding_box_center():
    # Test case 1: center of bounding box (2, 3, 5, 6)
    center_x, center_y = calculate_bounding_box_center(2, 3, 5, 6)
    assert math.isclose(center_x, 4.5, rel_tol=1e-2)
    assert math.isclose(center_y, 6.0, rel_tol=1e-2)
    print(center_x,center_y)

    # Test case 2: center of bounding box (0, 0, 0, 0)
    center_x, center_y = calculate_bounding_box_center(0, 0, 0, 0)
    assert center_x == 0.0
    assert center_y == 0.0

if __name__ == "__main__":
    # Run the tests
    test_calculate_distance()
    test_calculate_bounding_box_center()
    print("All tests passed.")
