# You may want to import your lab2_2 module
# from lab2_2 import *
import lab2_2

def dec_to_bin_list(dec_num):
    # DO NOT modify this function
    """
    (num)-> List[num]

    Function that converts decimal integer number to binary

    Usage: bin_list = dec_to_bin_list( dec_num )
    Input: dec_num is an integer number
    Output: bin_list is a list with four elements (0's and 1's), in the order of most significant bit to least significant bit

    The function assumes that dec_num is an integer.

    Inputs that are not in the range 0 to 15 will produce the same output as dec_num - 16*k where
    k is an integer that makes dec_num - 16*k attain a value from 0 to 15.

    >>> dec_to_bin_list(8)
    [1, 0, 0, 0]
    
    >>> dec_to_bin_list(16)
    [0, 0, 0, 0]
    """

    bin_list = []
    # start building the bin_list from the least significant bit
    # only need 4 bits
    while len(bin_list) < 4: 
        curr_bit = dec_num % 2
        bin_list.append(int(curr_bit))
        dec_num = (dec_num - curr_bit)/2
 
    return list(reversed(bin_list))

def bin_list_to_dec(bin_list):
    # DO NOT modify this function
    '''
    (List[int]->int)

    Returns the decimal value of the input 4-bit number represented by bin_list.

    >>> bin_list_to_dec([1, 0, 0, 0])
    8
    '''
    dec = 0
    for i in range(len(bin_list)-1,-1, -1):
        dec += bin_list[i]*2**(len(bin_list)-i-1)
    return int(dec)

def add_two_bin_nums(four_bit_num1, four_bit_num2):
    '''
    (list[int]) -> list[int]

    Initializes list for the sum of two bin nums, runs loop to add values if sum is less than 2 and
    carry over the 1 if the sum of the indices is greater than 2

    >>>add_two_bin_nums([0,0,1,1], [0,1,0,1])
    [1,0,0,0]
    >>>add_two_bin_nums([0,1,1,0], [1,1,0,0])
    [0,0,1,0] 
    '''
    bin_sum = [0, 0, 0, 0]
    carry_over = 0

    for i in range(3, -1, -1):
        if (four_bit_num1[i] + four_bit_num2[i] + carry_over) < 2:
            bin_sum[i] = four_bit_num1[i] + four_bit_num2[i] + carry_over
            carry_over = 0
        elif (four_bit_num1[i] + four_bit_num2[i] + carry_over) == 3:
            bin_sum[i] = 1
            carry_over = 1
        else:
            bin_sum[i] = 0
            carry_over = 1

    return bin_sum

def check_bit_add(four_bit_num1, four_bit_num2, result):
    '''
    (list) -> list

    First, the function finds the sum of the binary addition of four_bit_num1 and four_bit_num2
    Then, it calls the error_indices function from part 2 to return the indices where the sum does 
    not match the result, if there are any.

    >>>check_bit_add([1,0,1,0], [0,1,0,1], [1,1,1,1])
    []
    >>>check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [0,1,0,1])
    [0,2]
    '''
    bit_sum = add_two_bin_nums(four_bit_num1, four_bit_num2)
    check_indices = lab2_2.error_indices(bit_sum, result)
    
    return check_indices

def check_dec_add(four_bit_num1, four_bit_num2):
    '''
    (list) -> int

    Begins by running the same code as the binary number addition function and
    calculates the sum of the 4 bit lists. Then the function checks if the
    carry_over value is 1, signifying if bit overflow occurs and returns the 
    desired int values.

    >>>check_dec_add([0,0,1,1], [0,1,0,1])
    1
    >>>check_dec_add([1,0,0,0], [1,0,0,0])
    0
    '''
    bin_sum = [0, 0, 0, 0]
    carry_over = 0

    for i in range(3, -1, -1):
        if (four_bit_num1[i] + four_bit_num2[i] + carry_over) < 2:
            bin_sum[i] = four_bit_num1[i] + four_bit_num2[i] + carry_over
            carry_over = 0
        elif (four_bit_num1[i] + four_bit_num2[i] + carry_over) == 3:
            bin_sum[i] = 1
            carry_over = 1
        else:
            bin_sum[i] = 0
            carry_over = 1

    if carry_over == 1:
        return 0
    else:
        return 1

def get_error_source(four_bit_num1, four_bit_num2, result):
    '''
    (list) -> int

    Checks if there is an error source at all, then checks if the error source is solely
    a bit overflow error and not an indices error, else return 2 as it is neither of the
    first two conditions.

    >>>get_error_source([0,0,0,0],[0,0,0,0],[0,0,0,0])
    0
    >>>get_error_source([1,0,0,1], [1,0,0,1], [0,0,1,0])
    1
    >>>get_error_source([1,0,0,1], [1,0,0,1], [1,0,1,0])
    2
    '''
    error_source = check_dec_add(four_bit_num1, four_bit_num2)
    bin_result = add_two_bin_nums(four_bit_num1, four_bit_num2)
    if error_source == 1 and lab2_2.packet_diff(bin_result, result) == 0:
        return 0
    elif error_source == 0 and lab2_2.packet_diff(bin_result, result) == 0:
        return 1
    else:
        return 2

if __name__ == "__main__":
    #  test your functions here
    print(add_two_bin_nums([0,0,1,1], [0,1,0,1]))
    print(add_two_bin_nums([0,1,1,0], [1,1,0,0]))
    print(add_two_bin_nums([1,1,1,0], [1,1,0,0]))
    print(check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [1,1,1,1]))
    print(check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [0,1,0,1]))
    print(check_bit_add([1, 1, 1, 1],[1, 1, 1, 1], [1,1,1,0]))
    print(check_dec_add([0,0,1,1], [0,1,0,1]))
    print(check_dec_add([1,0,0,0], [1,0,0,0]))
    print(get_error_source([0,0,0,0], [0,0,0,0], [0,0,0,0]))
    print(get_error_source([1,0,0,1], [1,0,0,1], [0,0,1,0]))
    print(get_error_source([1,0,0,1], [1,0,0,1], [1,0,1,0]))
    # num 1 and num 2 should be positive integers less than 16

    dec1 = int(input('Num 1: '))
    dec2 = int(input('Num 2: '))
    
    bin1 = dec_to_bin_list(dec1)
    bin2 = dec_to_bin_list(dec2)

    bin_result = add_two_bin_nums(bin1, bin2) # to test your add_two_nums
    #bit_result = check_bit_add([1, 0, 1, 0],[0, 1, 0, 1], [1,1,1,1])    
    #print(bit_result)
    # makes the answer sometimes incorrect (emulates a bug that is not solely due to bit overflow)
    bin_result.sort()

    # alternate method of messing up the result
    # bin_result = list(reversed(bin_result))

    dec_result = bin_list_to_dec(bin_result)
    
    print('{} + {} = {}'.format(dec1, dec2, dec_result))

    # for testing your get_error_source, you may wish to comment this section initially
    if dec_result != dec1 + dec2:
        error_source = get_error_source(bin1, bin2, bin_result)
        if error_source == 0:
            print('Correct')
        elif error_source == 1:
            print('Bit overflow error')
        elif error_source == 2:
            print('Addition error')
        else:
            print('Unknown error code')
