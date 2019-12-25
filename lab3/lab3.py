import utilities

def rotate_90_degrees(image_array, direction = 1): #remember to write docstrings this function is good
    #1 for clock_wise. -1 for anticlockwise
    '''
    (list) -> list

    This function first checks if the given image in list form is grayscale or rgb, and the direction it is to be rotated. Then, the
    function takes each of the values in the original list, sets them to a new index in a new list which corresponds to the direction 
    of rotation.

    >>>rotate_90_degrees([[1,1,0],[0,0,0],[0,0,1]], 1)
    [[0,0,1],[0,0,1],[1,0,0]]

    >>>rotate_90_degrees([[1,1,0],[0,0,0],[0,0,1]], -1)
    [[0,0,1],[1,0,0],[1,0,0]]
    '''
	
    row_total = len(image_array)
    column_total = len(image_array[0])
    output_array = []

    if direction == -1 and isinstance(image_array[0][0], list) == True:
        for i in range(0, row_total):
            output_array.append([])
            for j in range(0, column_total):
                output_array[i].append([])
                for k in range(0,3):
                    output_array[i][j].append([])
                    output_array[i][j][k] = image_array[j][(column_total-(i+1))][k] 
    elif direction == 1 and isinstance(image_array[0][0], list) == True: #clockwise
        for j in range(0, column_total): #loops through all the columns
            output_array.append([])
            for i in range(0, row_total): #loops through all the rows
                output_array[j].append([])
                for k in range(0,3): #loops through all the r,g,b values
                    output_array[j][i].append([])
                    output_array[j][i][k] = image_array[(row_total-(i+1))][j][k] #sets first value in column j as the last value of column j and so on
    elif direction == -1 and isinstance(image_array[0][0], list) == False: #grayscale images, anticlockwise
        for i in range(0, row_total): #loops through all the rows
            output_array.append([])
            for j in range(0, column_total): #loops through all the columns
                output_array[i].append([])
                output_array[i][j] = image_array[j][(column_total-(i+1))]
    elif direction == 1 and isinstance(image_array[0][0], list) == False: #grayscale images, clockwise
        for j in range(0, row_total): #loops through all the rows
            output_array.append([])
            for i in range(0, column_total): #loops through all the columns
                output_array[j].append([])
                output_array[j][i] = image_array[(row_total-(i+1))][j]
    
    return output_array

def flip_image(image_array, axis = 0): #axis originally 0 flip_image(image_array, axis = 0) this works
	#axis = -1 (along x = y), 0 along y, 1 along x
	
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

    '''
    (list) -> list

    This function takes the original image in list form, checks if it is rgb or grayscale and the axis along which the image is
    to be flipped. Then the values in the original list are set in a new list with indices corresponding to the axis of the flip.

    >>>flip_image([[1,1,0],[0,0,0],[0,0,1]],- 1)
    [[1,0,0],[0,0,1],[0,0,1]]
    '''
    row_total = len(image_array)
    output_array = []
    
    if isinstance(image_array[0][0], list) == True:
        if axis == -1:
            for i in range(0, row_total): #axis = -1 (x=y axis):
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[(row_total-(j+1))][(row_total-(i+1))][k]
        elif axis == 0:
            for i in range(0, row_total): #axis = 0 (y-axis)
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[i][(row_total-(j+1))][k]
        elif axis == 1:
            for i in range(0, row_total): #axis = 1 (x-axis)
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[(row_total-(i+1))][j][k]
    else: #for grayscale images
        if axis == -1:
            for i in range(0, row_total): #axis = -1 (x=y axis):
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    output_array[i][j] = image_array[(row_total-(j+1))][(row_total-(i+1))]
        elif axis == 0:
            for i in range(0, row_total): #axis = 0 (y-axis)
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    output_array[i][j] = image_array[i][(row_total-(j+1))]
        elif axis == 1:
            for i in range(0, row_total): #axis = 1 (x-axis)
                output_array.append([])
                for j in range(0, row_total):
                    output_array[i].append([])
                    output_array[i][j] = image_array[(row_total-(i+1))][j]
    
			
    return output_array

def invert_grayscale(image_array): #invert grayscale works

    '''
    (list) -> list

    This function takes a grayscale image, creates a new list with inverted list values from 255 to 0 and looks at each index in of
    the original image in list form and appends the inverted value into the output_array in the same index.

    >>>invert_grayscale([[1,1,0],[0,0,0],[0,0,1]])
    [[254,254,255],[255,255,255],[255,255,254]]
    '''
    row_total = len(image_array)
    column_total = len(image_array[0])
    inverted_list = []
    output_array = []

    for m in range (255, -1, -1):
        inverted_list.append(m)

    for i in range(0, row_total): 
                output_array.append([])
                for j in range(0, column_total):
                    output_array[i].append([])
                    output_array[i][j] = inverted_list[image_array[i][j]]

    return output_array

def crop(image_array, direction, n_pixels): #rgb works, crop works
	
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################
    '''
    (list) -> list

    Takes the original image in list form, checks if it is rgb or grayscale, the direction and the number of pixels to be
    cropped. Then appends only the values that are not cropped out of the original image to a new list.

    >>>crop([[1,1,0],[0,0,0],[0,0,1]], left, 1)
    [[1,0],[0,0],[0,1]]
    '''
    row_total = len(image_array)
    column_total = len(image_array[0])
    output_array = []
    #check if n pixels exceeds image direction probably
    if isinstance(image_array[0][0], list) == True:
        if direction == 'left':
            for i in range (0, row_total):
                output_array.append([])
                for j in range(0, column_total - n_pixels): #loops through all the columns
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[i][n_pixels + j][k]
        elif direction == 'right':
            for i in range (0, row_total):
                output_array.append([])
                for j in range(0, column_total - n_pixels): #loops through all the columns
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[i][j][k]
        elif direction == 'down':
            for i in range (0, row_total - n_pixels):
                output_array.append([])
                for j in range(0, column_total): #loops through all the columns
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[i][j][k] #start at row n_pixels      
        elif direction == 'up':
            for i in range (0, row_total - n_pixels):
                output_array.append([])
                for j in range(0, column_total): #loops through all the columns
                    output_array[i].append([])
                    for k in range(0,3): #loops through all the r,g,b values
                        output_array[i][j].append([])
                        output_array[i][j][k] = image_array[n_pixels + i][j][k] #start at row n_pixels 
    else: #grayscale
        if direction == 'left':
            for i in range (0, row_total):
                output_array.append([])
                for j in range(0, column_total - n_pixels): #loops through all the columns
                    output_array[i].append([])
                    output_array[i][j] = image_array[i][n_pixels + j]
        elif direction == 'right':
            for i in range (0, row_total):
                output_array.append([])
                for j in range(0, column_total - n_pixels): #loops through all the columns
                    output_array[i].append([])
                    output_array[i][j] = image_array[i][j]
        elif direction == 'down':
            for i in range (0, row_total - n_pixels):
                output_array.append([])
                for j in range(0, column_total): #loops through all the columns
                    output_array[i].append([])
                    output_array[i][j] = image_array[i][j] #start at row n_pixels      
        elif direction == 'up':
            for i in range (0, row_total - n_pixels):
                output_array.append([])
                for j in range(0, column_total): #loops through all the columns
                    output_array[i].append([])
                    output_array[i][j] = image_array[n_pixels + i][j] #start at row n_pixels   

    return output_array

def rgb_to_grayscale(rgb_image_array): # this works

	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

    '''
    (list) -> list

    This function converts an rgb image to a grayscale image. It takes each rgb value, multiplies them with a corresponding grayscale 
    conversion factor and sums them to get the value in the index for the resulting grayscale image.

    >>>rgb_to_grayscale([[[100,100,100]]])
    [[[99.99]]]

    '''
    row_total = len(rgb_image_array)
    column_total = len(rgb_image_array[0])
    output_array = []

    for i in range(0, row_total):
            output_array.append([])
            for j in range(0, column_total):
                output_array[i].append([])
                output_array[i][j] = (rgb_image_array[i][j][0] * 0.2989) + (rgb_image_array[i][j][1] * 0.5870) + (rgb_image_array[i][j][2] * 0.1140)

    return output_array

def invert_rgb(image_array):
	#####################################
	##########YOUR CODE GOES HERE########
	#####################################

    '''
    (list) -> list

    This function creates a new list for all the inverted values from 255 to 0, and changes the rgb values inside the original image
    list accordingly.

    >>>invert_rgb([[[1,1,1]]])
    [[[254,254,254]]]
    '''
    row_total = len(image_array)
    column_total = len(image_array[0])
    output_array = []
    inverted_list = []


    for m in range (255, -1, -1):
        inverted_list.append(m)

    for i in range(0, row_total):
            output_array.append([])
            for j in range(0, column_total):
                output_array[i].append([])
                for k in range(0,3): #loops through all the r,g,b values
                    output_array[i][j].append([])
                    output_array[i][j][k] = inverted_list[image_array[i][j][k]]

    return output_array


if (__name__ == "__main__"):
    filename = 'robot.png'
    robot_list = utilities.image_to_list(filename)
    rotated_robot_list = flip_image(robot_list, axis = 0)
    utilities.write_image(rotated_robot_list, 'invertedpikachu0.png')
    rotated_robot_list = flip_image(robot_list, axis = 1)
    utilities.write_image(rotated_robot_list, 'invertedpikachu1.png')
    rotated_robot_list = flip_image(robot_list, axis = -1)
    utilities.write_image(rotated_robot_list, 'invertedpikachu-1.png')
    '''
    robot_list = utilities.image_to_list(filename)
    rotated_robot_list = invert_rgb(robot_list)
    utilities.write_image(rotated_robot_list, 'invertedpikachu.png')
    robot_list = utilities.image_to_list(filename)
    rotated_robot_list = crop(robot_list, "up", 150)
    utilities.write_image(rotated_robot_list, 'ucroppedpikachu.png')
    rotated_robot_list = crop(robot_list, "left", 150)
    utilities.write_image(rotated_robot_list, 'lcroppedpikachu.png')
    rotated_robot_list = crop(robot_list, "right", 150)
    utilities.write_image(rotated_robot_list, 'rcroppedpikachu.png')
    rotated_robot_list = crop(robot_list, "down", 150)
    utilities.write_image(rotated_robot_list, 'dcroppedpikachu.png')
    robot_list = utilities.image_to_list(filename)
    rotated_robot_list = rgb_to_grayscale(robot_list)
    utilities.write_image(rotated_robot_list, 'grayscalepikachu.png')
    robot_list = utilities.image_to_list(filename)
    rotated_robot_list = flip_image(robot_list, 0)
    utilities.write_image(rotated_robot_list, 'flippedpikachu.png')
    robot_list = utilities.image_to_list("grayscalepikachu.png")
    rotated_robot_list = invert_grayscale(robot_list)
    utilities.write_image(rotated_robot_list, 'invertedgrayscalepikachu.png.png')
   '''

   


