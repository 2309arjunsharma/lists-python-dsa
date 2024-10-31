def find_max_element(nums):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # TODO: Implement this function
    maximum=nums[0]
    for i in nums:
        if i>maximum:
            maximum=i
    return maximum
print(find_max_element([3,5,2,9,6]))