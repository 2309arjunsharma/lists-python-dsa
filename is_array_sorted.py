def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    
print(is_sorted([1,2,3,4,5]))