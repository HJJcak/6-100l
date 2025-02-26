# ex_1.py

import numpy as np

def GuessSqrtOfANumber(number:int, init_guess:int, tolerance:float):
    """Computes the square root of a number using the Newton-Raphson method.
    
    Args:
    number: int, the number to compute the square root of.
    init_guess: int, the initial guess for the square root.
    tolerance: float, the tolerance for the square root.

    Return:
    guess: float, the square root of the number.
    """
    # Check if 
    sqrtofguess = init_guess
    guess = sqrtofguess ** 2

    # Loop until the guess is within the tolerance.
    while abs(guess - number) > tolerance:
        sqrtofguess = (sqrtofguess + number / sqrtofguess) / 2
        guess = sqrtofguess ** 2

    return sqrtofguess

if __name__ == "__main__":
    number = int(input("Type number:"))
    init_guess = float(input("Type initial guess:"))
    tolerance = 1e-5
    guess = GuessSqrtOfANumber(number, init_guess, tolerance)
    print(f"The square root of {number} is {guess}.")    


