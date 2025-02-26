# ex_3.py

def CheckLettersInString(chars:list[str], aim:str)->bool:
    """Check if the characters in the list are in the string

    Args:
    chars: list[str], the list of characters to check
    aim: str, the string to check

    Return:
    result: bool, True if any characters in chars are in the string, False otherwise
    """
    for char in chars:
        if char in aim:
            return True
    return False

def CountUniqueLettersInString(aim:str)->int:
    """Count the number of unique letters in the string

    Args:
    aim: str, the string to check

    Return:
    result: int, the number of unique letters in the string
    """
    unique_aim = []
    for char in aim:
        if char not in unique_aim:
            unique_aim.append(char)
    return len(unique_aim)

if __name__ == "__main__":

    # chars = list(input("Type characters:"))
    # aim = input("Type a string:")
    # result = CheckLettersInString(chars, aim)
    # print(f"Some characters in {chars} are in the string: {result}.")

    aim = input("Type a string:")
    result = CountUniqueLettersInString(aim)
    print(f"The number of unique letters in the string is {result}.")
