# ex_10.py
from typing import Callable

Function = Callable[[int], bool]

def apply(criteria:Function, n:int)->int:
    """Check how many ints from 0 to n (inclusive) match thecriteria

    Args:
        criteria(f): A function that takes an int and returns a bool
        n(int): The upper bound of the range to check
    
    Returns:
        int: The number of ints from 0 to n that match the criteria
    """
    count = 0
    for i in range(0, n + 1):
        if criteria(i):
            count += 1
    
    return count

def make_ordered_list(n:int)->list:
    """Return a list of ints from 0 to n (inclusive)

    Args:
        n(int): The upper bound of the range to generate
    
    Returns:
        list: A list of ints from 0 to n
    """
    return list(range(n + 1))

def remove_elem(L:list, e)->list:
    """Return a new list with all occurrences of e removed
    
    Args:
        L(list): The list to remove elements from
        e: The element to remove
    
    Returns:
        list: A new list with all occurrences of e removed
    """
    for i in L:
        if i == e:
            L.remove(i)
    
    return L

def count_words(sen:str)->int:
    """Return the number of words in a sentence

    Args:
        sen(str): The sentence to count words in
    
    Returns:
        int: The number of words in the sentence
    """
    return len(sen.split(" "))

def sort_words(sen:str)->str:
    """Return the words in a sentence sorted alphabetically

    Args:
        sen(str): The sentence to sort

    Returns:
        str: The words in the sentence sorted alphabetically
    """
    return " ".join(sorted(sen.split(" ")))

def all_true(n:int, Lf:list[Function])->bool:
    """Return True if all functions in Lf return True for n, False otherwise

    Args:
        n(int): The number to check
        Lf(list): A list of functions that take an int and return a bool
    
    Returns:
        bool: True if all functions in Lf return True for n, False otherwise
    """
    for f in Lf:
        if not f(n):
            return False
    
    return True

def remove_all(L:list, e)->None:
    """Change given list with all occurrences of e removed

    Args:
        L(list): The list to remove elements from
        e: The element to remove
    
    Returns:
        None
    """
    # return [i for i in L if i != e]
    tmp = L[:]
    L.clear()
    for i in tmp:
        if i != e:
            L.append(i)

    return None

if __name__ == "__main__":
    # n = int(input("Enter a number: "))
    # print(apply(lambda x: x % 2 == 0, n))
    pass