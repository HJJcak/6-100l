# ex_6.py
from typing import Callable

# define the type of a function
FuncType = Callable[[float|int], float]

def Derivative(f:FuncType, x:float|int, h=1e-6)->float:
    """Calculate the derivative of a function at a point using the definition of the derivative
    
    Args:
    f: function
    x: point at which to calculate the derivative
    h: small number to calculate the derivative

    Returns:
    The value of the derivative at x, or None if the calculation fails.
    """
    try:
        return (f(x+h) - f(x-h)) / (2*h)
    except Exception as e:
        print(f"Error calculating derivative: {e}")
        return None

def QuadraticDerivative(f:FuncType, x:float|int, h=1e-6)->float:
    """Calculate the second derivative of a function at a point using the definition of the derivative
    
    Args:
    f: function
    x: point at which to calculate the derivative
    h: small number to calculate the derivative

    Returns:
    The value of the second derivative at x, or None if the calculation fails.
    """
    try:
        return (f(x+h) - 2*f(x) + f(x-h)) / h**2
    except Exception as e:
        print(f"Error calculating quadratic derivative: {e}")
        return None

def QuadraticApproximation(f:FuncType, x:float|int, x0:float|int)->float:
    """Calculate the quadratic approximation of a function at a point

    Args:
    f: function
    x: point at which to calculate the quadratic approximation
    x0: point to help calculate the quadratic approximation

    Returns:
    The value of the quadratic approximation at x, or None if the calculation fails.
    """
    try:
        return f(x0) + Derivative(f, x0) * (x-x0) + 0.5 * QuadraticDerivative(f, x0) * (x-x0)**2
    except Exception as e:
        print(f"Error calculating quadratic approximation: {e}")
        return None

def Newton_method(f:FuncType, x:float|int, tol:float=1e-6, max_iter:int=100)->float:
    """Calculate the root of a function using the Newton method.

    Args:
        f: The function for which to find the root.
        x: Initial guess.
        tol: Tolerance for convergence.
        max_iter: Maximum number of iterations.

    Returns:
        The approximate root of the function, or None if the method fails to converge.
    """
    try:
        for i in range(max_iter):
            x = x - f(x) / (Derivative(f, x) + 1e-6)
            
            if abs(f(x)) < tol:
                return x
        
        raise ValueError("Newton method did not converge within the maximum number of iterations.")
    
    except Exception as e:
        print(f"Error calculating Newton method: {e}")
        return None

def GetEvenIndexOfAString(s:str)->str:
    """Get the even index of a string

    Args:
    s: string

    Returns:
    The even index of the string
    """
    try:
        return s[::2]
    except Exception as e:
        print(f"Error getting even index of a string: {e}")
        return None