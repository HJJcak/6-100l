# ex_9.py
from ex_7 import BisectoinSearchForRoot

def count_nums_with_sqrt_close_to (n:int, epsilon:float)->int:
    """Returns how many integers have a square root within epsilon of n

    Args:
        n is an int > 2
        epsilon is a positive number < 1
    
    Returns:
        The number of integers i such that |sqrt(i) - n| < epsilon
    """
    count = 0
    for i in range(int((n - epsilon)**2) - 1, int((n + epsilon)**2) + 1):
        if abs(BisectoinSearchForRoot(i)[0] - n) <= epsilon:
            count += 1
    
    return count

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    epsilon = float(input("Enter the value of epsilon: "))
    print(f"The number of integers i such that |sqrt(i) - {n}| < {epsilon} is: {count_nums_with_sqrt_close_to(n, epsilon)}")
