def packet_size(packet):
    ''' 
    (list) -> int

    this function takes the given list and returns the number of indexes in that
    list as the size

    >>>packet_size([0,1,0,1])
    4
    '''
    return len(packet)

def error_indices(packet1, packet2):
    ''' 
    (list, list) -> list

    this function takes the list of packet1 and packet2 and compares each index of both to
    check if they are equal, if they are not, it appends the index value to a the list
    error_indices

    >>>error_indices([0,1,1,1], [1,1,0,1])
    [0,2]
    >>>error_indices([1,1,0,1], [1,1,0,1])
    []
    '''
    error_indices = []

    for i in range(0, len(packet1)):
        if packet1[i] != packet2[i]:
            error_indices.append(i)

    return error_indices

def packet_diff(packet1, packet2):
    '''
    (list, list) -> int

    takes the list of error indices and returns the length of that list

    >>>find_packet_diff([0,1,0,1], [1,1,0,1])
    1
    >>>find_packet_diff([0,1,1,0], [0,1,1,0])
    0
    '''
    return len(error_indices(packet1, packet2))

if __name__ == "__main__":
    # test your bit error rate detector here
    print(packet_size([0,1,0,1]))
    print(error_indices([0,1,1,1], [1,1,0,1]))
    print(error_indices([1,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,0,1], [1,1,0,1]))
    print(packet_diff([0,1,1,0], [0,1,1,0]))
    packet_sent = [0, 1, 1, 1]
    packet_received = [1, 1, 1, 1]
