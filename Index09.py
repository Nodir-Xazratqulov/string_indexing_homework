def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if int(s) == int(s):
        return s
    elif str(s) != int(s):
        return -1
print(main('h'))