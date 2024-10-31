def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    l,r=0,len(lst)-1
    while l<r:
        if lst[l]!=lst[r]:
            return False
        l+=1 
        r-=1 
    return True
print(is_palindrome([7,8,9,8,7]))
