# ex_11.py

from typing import Callable

# L = [1, 2, 3, 4, 5, 6, 2]
# L.remove(2) 
# -> [1, 3, 4, 5, 6, 2]
# del(L[1])
# -> [1, 4, 5, 6, 2]
# L.pop()
# -> [1, 4, 5, 6]

def remove_all(L:list, e)->None:
    """Remove all elements e from list L.

    Args:
        L(list): the list to remove elements from.
        e(any): the element to remove
    
    Returns:
        None
    """
    # while e in L:
    #   L.remove(e)
    # False because the list is modified in place and the index is not updated.

    L_c = L[:]
    for i in L_c:
        if i == e:
            L.remove(i)



