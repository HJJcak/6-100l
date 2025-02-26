# ex_8.py

def Is_even(i:int)->bool:
    """Return True if i is even, False otherwise.

    Args:
        i(int): An integer
    
    Returns:
        bool: True if i is even, False otherwise.
    """
    return i % 2 == 0

def Div_by(n:int, d:int)->bool:
    """Return True if n is divisible by d, False otherwise.

    Args:
        n (int): An integer.
        d (int): An integer.
    
    Returns:
        bool: True if n is divisible by d, False otherwise.
    """
    return n % d == 0

def Sum_odd(a:int, b:int)->int:
    """Return the sum of all odd numbers between a and b.

    Args:
        a(int): An integer
        b(int): An integer
    
    Returns:
        int: the sum of all odd numbers between a and b
    """
    sum = 0

    for n in range(a, b + 1):
        if not Is_even(n):
            sum += n
        else:
            pass
    
    return sum

def Is_palindrome(s:str)->bool:
    """Retrun True if this string is a palingrome, False otherwise.

    Args:
        s(str): a string
    
    Returns:
        bool: True if this string is a palingrome, False otherwise.
    """
    i = 0

    while i < (len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
        else:
            i += 1
    
    return True

if __name__ == "__main__":
    # a = int(input("Please type the lower number: "))
    # b = int(input("Please type the upper number: "))
    # print(f"The sum of all odd numbers between {a} and {b} is {Sum_odd(a, b)}")
    s = input("Please type a string to check if it is a palindrome: ")
    if Is_palindrome(s):
        print("Yes, it is")
    else:
        print("No, it is not")

