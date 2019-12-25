# ESC180 Lab 1
# Connected Cows
# DO NOT modify any function or argument names
import math

def find_euclidean_distance(x1, y1, x2, y2):
    """
    This function takes the points given, finds the value between the two x points, 
    then finds the value between the two y points, squares both, and roots the answer
    to find the distance between the two points.
    """ 
    distance_between_points = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
    return round(distance_between_points, 2)	
    #function body
	


def is_cow_within_bounds(cow_position, boundary_points):
    """
    this function checks to see if the cow position coordinates are between the x and y coordinates of the boundary points 
    """
    if cow_position[0] > boundary_points[3][0] and cow_position[0] < boundary_points[2][0]:
        if cow_position[1] > boundary_points[3][1] and cow_position[1] < boundary_points[0][1]:
            return 1
        else:
            return 0
    else:
        return 0
    
    #function body


def find_cow_distance_to_boundary(cow_position, boundary_point):
    """
    same equation as finding the euclidean distance except using the list format for x and y values
    """
    distance_to_boundary  = (((cow_position[0] - boundary_point[0]) ** 2) + ((cow_position[1] - boundary_point[1]) ** 2)) ** (1 / 2)
    return round(distance_to_boundary, 2)
    #function body


def find_time_to_escape(cow_speed, cow_distance):
    """
    the function checks whether the cow is moving, if the cow is moving, it divides the cow's distance to the boundary by the cows speed to
    find the time it takes for the cow to reach the boundary, if cow_speed = 0 then the function returns -1
    """
    if cow_speed > 0:
        time_to_escape = cow_distance / cow_speed
        return round(time_to_escape, 2)
    else:
        return -1

    #function body


def report_cow_status(cow_position1, cow_position2, delta_t, boundary_points):
    """
    first, find cow speed
    find whether cow is in bounds at both positions
    if cow is within bounds at both positions, find distance from position2 to each boundary's x and y positions
    and use conditionals to determine shortest distance and then use time to escape function to calculate the
    time it would take the cow to escape through the shortest path
    if not, function checks if cow is out of bounds at both positions and calculate distance to boundary_points[0] and divide
    by cow_speed to find the time it takes for the cow to get to the boundary point
    if not, function checks if cow is going from out of boundary to within boundary and returns 1
    else function returns 0    
    """
    cow_speed = find_euclidean_distance(cow_position1[0], cow_position1[1], cow_position2[0], cow_position2[1]) / delta_t

    cow_position1_bound_status = is_cow_within_bounds(cow_position1, boundary_points)
    cow_position2_bound_status = is_cow_within_bounds(cow_position2, boundary_points)
										
    if cow_position1_bound_status == 1 and cow_position2_bound_status == 1:
        cow_path1 = abs(cow_position2[0] - boundary_points[0][0]) #uses abs() to compare positive distances to the boundary
        cow_path2 = abs(cow_position2[0] - boundary_points[1][0])
        cow_path3 = abs(cow_position2[1] - boundary_points[0][1])
        cow_path4 = abs(cow_position2[1] - boundary_points[3][1])
        if cow_path1 <= cow_path2:
            if cow_path1 <= cow_path3:
                if cow_path1 <= cow_path4:
                    time_to_escape = find_time_to_escape(cow_speed, cow_path1)
                    return time_to_escape
                else:
                    time_to_escape = find_time_to_escape(cow_speed, cow_path4)
                    return time_to_escape
            elif cow_path3 <= cow_path4:
                time_to_escape = find_time_to_escape(cow_speed, cow_path3)
                return time_to_escape
        elif cow_path2 <= cow_path3:
            if cow_path2 <= cow_path4:
                time_to_escape = find_time_to_escape(cow_speed, cow_path2)
                return time_to_escape
    elif cow_position1_bound_status == 0 and cow_position2_bound_status == 0:
        distance_to_boundary = find_cow_distance_to_boundary(cow_position2, boundary_points[0])
        time_to_boundary = distance_to_boundary / cow_speed
        return round(time_to_boundary, 2)
    elif cow_position1_bound_status == 0 and cow_position2_bound_status == 1:
        return -1
    else:
        return 0
    #function body


if __name__ == '__main__':
    # Test your code by running your functions here, and printing the
    # results to the terminal.
    # This code will not be marked
    print('Testing functions...')
    test_distance = find_euclidean_distance(3.0, 3.0, 2.0, 5.0)
    print(test_distance)
    test_distance = find_euclidean_distance(5.0, 2.0, 4.0, 2.0)
    print(test_distance)
    cow_bound_status = is_cow_within_bounds([3, 3], [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(cow_bound_status)
    cow_bound_status = is_cow_within_bounds([3, 3], [[4, 4], [5, 4], [5, 2], [4, 2]])
    print(cow_bound_status)
    cow_distance_to_boundary = find_cow_distance_to_boundary([2, 2], [0, 1])
    print(cow_distance_to_boundary)
    cow_distance_to_boundary = find_cow_distance_to_boundary([3, 3], [2, 5])
    print(cow_distance_to_boundary)
    cow_time_to_escape = find_time_to_escape(0, 100)
    print(cow_time_to_escape)
    cow_time_to_escape = find_time_to_escape(9.0, 111.0)
    print(cow_time_to_escape)
    cow_status = report_cow_status([3, 3], [4, 4], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(cow_status)
    cow_status = report_cow_status([0, 0], [3, 7], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(cow_status)
    cow_status = report_cow_status([0, 0], [3, 3], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(cow_status)
    cow_status = report_cow_status([3, 3], [3, 6], 10.0, [[2, 5], [5, 5], [5, 1], [2, 1]])
    print(cow_status)
#  test_distance should be 2.24
