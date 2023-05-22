def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer

    """
    

    if s.find('*',0,10) == -1:
        return False
    
    return s.find('*',0,10)
    
print(main('24*4'))
        