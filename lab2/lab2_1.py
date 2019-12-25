import math

def vector_from_points(p1, p2):
    ''' 
    (list,list) -> list

    this function is a loop that goes through each index of the length of the given list
    p1 and subtracts the same index of p1 from p2, appending the value to a new list,
    vectorp1p2

    >>>vector_from_points([0, 0], [1, 2])
    [1,2]
    >>>vector_from_points([3,-1,0], [10,0,1])
    [7,1,1]
    '''
    vectorp1p2 = [] #initialize empty list
    for i in range(0, len(p1)):
        vectorp1p2.append(p2[i] - p1[i])
    return vectorp1p2
    
def vector_length(v):
    ''' 
    (list) -> float

    this function takes checks if the list is empty, and if it is not, runs a loop that 
    adds the square of each element in v and then square roots the sum to return the 
    magnitude of v

    >>>vector_length([2, 1])
    2.23606797749979
    >>>vector_length([])
    -1
    '''
    upper_index = len(v)
    v_sum = 0

    if upper_index > 0:
        for i in range(0, upper_index):
            v_sum = v_sum + (v[i] ** 2)
        return math.sqrt(v_sum)
    else:
        return -1 

def angle_between(v, w):
    ''' 
    (list,list) -> float

    this function runs a loop that calculates the dot product of the two lists, then takes     the dot product, divides it by the vector length of vector v multiplied by vector w
    and uses method math.acos to find the angle between the vectors in radians. This is
    then multiplied by 180/math.pi to find the angle in degrees.

    >>>angle_between([-1], [2])
    180.0
    >>>angle_between([0,1,0,1], [1,3,4,5])
    '''
    dot_product = 0
    for i in range(0, len(v)):
        dot_product = dot_product + (v[i] * w[i])
    return  math.acos(dot_product / (vector_length(v) * vector_length(w))) * (180/math.pi)
      

def dot_product(v,w):
    '''
    (list, list) -> float

    This function takes two lists v and w and multiplies the each index from one list with other and
    sums all the values to obtain the dot product of both lists.

    >>>dot_product([-1], [2])
    -2
    >>>dot_product([0,1,0,1], [1,3,4,5)
    8
    '''
    dot_product = 0
    for i in range(0, len(v)):
        dot_product = dot_product + (v[i] * w[i])
    return dot_product    

def unit_vector(v):
    ''' 
    (list) -> list

    this function takes each index of the given list, divides it by the vector length of 
    the list and appends it to a new list as values of the unit vector

    >>>unit_vector([2, 1])
    [0.8944271909999159, 0.4472135954999579)
    >>>unit_vector([])
    []
    '''
    unit_vector = []
    for i in range(0, len(v)):
        unit_vector.append(v[i] / vector_length(v))
    
    return unit_vector

def cross_product(v,w):
    ''' 
    (list, list) -> list

    the function first checks if the lists have more than 3 elements, if the do not it runs loops
    which append 0's to the lists of both v and w to ensure that they are 3 element lists. the
    function then calculates each value in the cross product and returns the 3 element cross
    product list.

    >>>cross_product([2, 8], [1, 4, 3])
    [24, -6, 0]
    >>>cross_product([1, 1, 1, 0], [1, 5.5])
    []
    '''
    if len(v) > 3 or len(w) > 3:
        return []
    else:
        for i in range(0, (3-len(v))):
            v.append(0)
        for j in range(0, (3-len(w))):
            w.append(0)
    cross_product = [(v[1] * w[2]) - (v[2] * w[1]), (v[2] * w[0]) - (v[0] * w[2]), (v[0] * w[1]) - (v[1] * w[0])]
    return cross_product

def scalar_projection(v,w):
    ''' 
    (list, list) -> float

    Calls dot_product function of v, w and divides it by the magnitude of v found by the function
    vector_length

    >>>scalar_projection([-2], [1.5])
    -1.5
    >>>scalar_projection([0,3], [1.5,2])
    2.0
    '''
    return dot_product(v, w) / vector_length(v)

def vector_projection(v,w):
    '''
    (list, list) -> list

    This function performs divides the dot product of vectors v and w by the magnitude squared of
    vector v, and multiplies by each index in list v, appending the result to a new list for the
    vector projection.

    >>>vector_projection([-2], [1.5])
    [1.5]
    >>>vector_projection([0,3], [1.5,2])
    [0.0, 2.0]
    '''
    vector_projection = []
    for i in range(0, len(v)):
        vector_projection.append(dot_product(v, w) / (vector_length(v) ** 2) * v[i])

    return vector_projection

if __name__ == "__main__":
    # test your vector operations here
    v1 = [0, -2, 3]
    v2 = [1, 1, 1]
    print(vector_from_points([0, 0], [1, 2]))
    print(vector_from_points([3, -1, 0], [10, 0, 1]))
    print(vector_length([2, 1]))
    print(vector_length([]))
    print(angle_between([-1], [2]))
    print(angle_between([0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([-1], [2]))
    print(dot_product([0, 1, 0, 1], [1, 3, 4, 5]))
    print(dot_product([0, 0], [0, 0]))
    print(unit_vector([2, 1]))
    print(unit_vector([]))
    print(cross_product([], [2]))
    print(cross_product([2, 8], [1, 4, 3]))
    print(cross_product([1, 1, 1], [5.5, 5.5, 5.5]))
    print(cross_product([1, 1, 1, 0], [1, 5.5]))
    print(scalar_projection([-2], [1.5]))
    print(scalar_projection([0, 3], [1.5, 2]))
    print(vector_projection([-2], [1.5]))
    print(vector_projection([0, 3], [1.5, 2]))
    #cross_product = cross_product([], [2])
    #print(cross_product)
    #vectorp1p2 = vector_from_points([0,0], [1,2])
    #print(vectorp1p2)
    #vector_length = vector_length([2, 1])
    #print(vector_length)
    #angle_between = angle_between([-1], [2])
    #print(angle_between)
