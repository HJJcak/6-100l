# ex_4.py

def FindTheCuberootOfANumber(number:int)->None:
    """Find the cube root of a number

    Args:
    number: int, the number to find the cube root of

    Return:
    result: int, the cube root of the number
    """
    
    for guess in range(abs(number) + 1):
        if guess**3 >= abs(number):
            break
    
    if guess**3 != abs(number):
        print("Do not find the cube root of given number")
    else:
        if number < 0:
            guess = -guess
        print(f"The cube root of {number} is {guess}")

def GetBinaryOfANumber(number:int)->str:
    """Get the binary representation of a number

    Args:
    number: int, the number to get the binary representation of

    Return:
    result: str, the binary representation of the number
    """
    
    result = ""
    if number < 0:
        isNeg = True
        number = abs(number)
    else:
        isNeg = False

    if number == 0:
        result = "0"
    while number > 0:
        result = str(number % 2) + result
        number = number // 2

    if isNeg:
        result = "-" + result
    return result

if __name__ == "__main__":
    number = int(input("Type a number:"))
    # FindTheCuberootOfANumber(number)
    print(GetBinaryOfANumber(number))