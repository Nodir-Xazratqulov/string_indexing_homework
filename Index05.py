def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    k=0
    i=0
    while i<len(s):
        if s[i].isdigit():
            k+=1
        i+=1
    return k
print(main('32x3z456sw'))