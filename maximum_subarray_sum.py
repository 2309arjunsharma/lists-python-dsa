def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    # Implement the function
    if not arr:
        return 0
    max_sum=0
    current_sum=float('-inf')
    for i in arr:
        max_sum=max(i,max_sum+i)
        current_sum=max(current_sum,max_sum)
    
    return current_sum
    #Alternative code
    #max_sum = arr[0]  
    #current_sum = arr[0]  
    #for i in range(1,len(arr)-1):
        #current_sum=max(arr[i],current_sum+arr[i])
        #max_sum=max(max_sum,current_sum)
    #return max_sum
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4,0]))
