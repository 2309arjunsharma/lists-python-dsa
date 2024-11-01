def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    # TODO: Implement this function
    return list(set(nums1) & set(nums2))
print(intersection([1,2,3],[1,3,4]))
print(intersection([1,2,3],[4,5,6]))
