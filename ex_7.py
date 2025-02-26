# ex_7.py

def BisectoinSearchForRoot(aim:float, tol:float=1e-5)->float:
    """Calculate the root of a float using the Bisection method.

    Args:
    aim: the aim number
    tol: the tolerance of the calculation

    Returns:
    The root of the aim, or None if the calculation fails and the number of guesses.
    """
    try:
        # define the initial interval
        if aim >= 1:
            low = 0
            high = aim
        else:
            low = aim
            high = 1
        guess = (low + high) / 2
        num_guess = 0

        # Bisection method
        while(abs(aim - guess**2) > tol):
            if guess**2 < aim:
                low = guess
            else:
                high = guess
            guess = (low + high) / 2.0
            num_guess += 1

        return guess, num_guess
    
    except Exception as e:
        print(f"Error calculating root: {e}")
        return None
    

if __name__ == "__main__":
    aim = float(input("Enter the value of the aim at the root: "))
    print(f"The root of the function is: {BisectoinSearchForRoot(aim)[0]}")
    print(f"Use {BisectoinSearchForRoot(aim)[1]} guesses to find the root.")