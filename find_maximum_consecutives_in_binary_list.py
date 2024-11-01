def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    c=0
    i=0
    for n in nums:
        if n==1:
            i+=1 
        else:
            c=max(c,i)
            i=0
    return max(c,i)
print(find_max_consecutive_ones([0,0,0,0]))
print(find_max_consecutive_ones([1,1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1]))