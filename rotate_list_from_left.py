def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # TODO: Implement this function
    if not ARR:
        return []
        k = k % len(ARR)
    for i in range(D,len(ARR)):
        last_element = ARR.pop()
        ARR.insert(0, last_element)
    
    return ARR
    
print(rotate_left([1,2,3,4,5,6],2))


