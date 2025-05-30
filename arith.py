def add(a: 'int', b: 'int') -> 'int':
    """Add 'a' to 'b'

    Args:
        a (int): This is an integer
        b (int): This is another integer

    Returns:
        int: Return an integer if both input values are ints;
        print a message otherwise
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print("Enter a valid integer.")
        
def sub(a: 'any', b: 'any') -> 'any':
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        return a - b



        