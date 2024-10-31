def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # TODO: Implement this function
    n=len(nums)
    sum1=n*(n+1)//2
    sum2=sum(nums)
    return sum1-sum2
print(find_missing_number([1,0,3]))