#ex_12.py

def g(x):
    """
    if x > 0 return True otherwise False

    Args:
        x(float): the input number
    
    Returns:
        Boolen
    """
    return (x > 0)

def h(x):
    """
    Return x**2

    Args:
        x(float): the input float
    
    Returns:
        y(float): x**2
    """
    return x**2

def f(L, g, h):
    """
    Create a new list for some condition

    Args:
        L(List): the given list
        g(function): the condition
        h(function): the transfer
    Returns:
        Lnew(List): the new list 
    """
    Lnew = []
    for element in L:
        if g(element):
            Lnew.append(h(element))
    
    return Lnew

#------equal to------#
L = [1, -1, 2, -2]
Lnew = [h(element) for element in L if g(element)]

#------#
def make_prod(a):
    def g(b):
        return a * b
    return g

if __name__ == "__main__":
    print(make_prod(2)(3))