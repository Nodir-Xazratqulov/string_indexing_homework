def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    f=s[4]
    return int(a)+int(b)+int(c)+int(d)+int(f)
print(main('12345'))