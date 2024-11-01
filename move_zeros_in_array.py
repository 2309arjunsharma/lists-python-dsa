def move_zeroes(arr):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # TODO: Implement this function
    count = 0 
    n = len(arr)
    for i in range(n):  
        if arr[i] != 0:  
            arr[count] = arr[i]
            count += 1  
    while count < n:  
        arr[count] = 0  
        count += 1  
    return arr
print(move_zeroes([0,1,0,3,12]))
