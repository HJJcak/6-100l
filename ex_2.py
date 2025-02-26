# ex_2.py

import numpy as np

def SaveAHome(yearly_salary:float, portion_saved:float, cost_of_dream_home:float, portion_down_payment:float=0.25, annual_rate:float=0.05):
    """ find the number of months it takes to save up for a down payment

    Args:
    yearly_salary: float, the yearly salary of the person
    portion_saved: float, the portion of the salary saved each month
    cost_of_dream_home: float, the cost of the dream home
    portion_down_payment: float, the portion of the cost of the dream home needed for a down payment
    annual_rate: float, the annual rate of return on the savings

    Return:
    months: int, the number of months it takes to save up for a down payment
    """
    # The amount of money saved each month
    amount_saved = 0
    # The number of months it takes to save up for a down payment
    mouths = 0

    # The main loop to calculate the number of months
    while amount_saved < cost_of_dream_home * portion_down_payment:
        amount_saved += yearly_salary / 12 * portion_saved + amount_saved * annual_rate / 12
        mouths += 1
    
    return mouths

def SaveAHomeUp1(yearly_salary:float, portion_saved:float, cost_of_dream_home:float,  semi_annual_raise:float, portion_down_payment:float=0.25, annual_rate:float=0.05):
    """ find the number of months it takes to save up for a down payment

    Args:
    yearly_salary: float, the yearly salary of the person
    portion_saved: float, the portion of the salary saved each month
    cost_of_dream_home: float, the cost of the dream home
    semi_annual_raise: float, the semi-annual raise of the salary every 6 mouths
    portion_down_payment: float, the portion of the cost of the dream home needed for a down payment
    annual_rate: float, the annual rate of return on the savings

    Return:
    months: int, the number of months it takes to save up for a down payment
    """
    # The amount of money saved each month
    amount_saved = 0
    # The number of months it takes to save up for a down payment
    mouths = 0

    # The main loop to calculate the number of months
    while amount_saved < cost_of_dream_home * portion_down_payment:
        amount_saved += yearly_salary / 12 * portion_saved + amount_saved * annual_rate / 12
        mouths += 1
        if mouths % 6 == 0:
            yearly_salary *= 1 + semi_annual_raise
    
    return mouths

def LowestrForHome(initial_deposit:float, cost_of_dream_home:float=800000, portion_down_payment:float=0.25):
    """ find the lowest annual rate to save up for a down payment in 3 years
    
    Args:
    initial_deposit: float, the initial deposit of the savings

    Return:
    annual_rate: float, the lowest annual rate to save up for a down payment in 3 years
    """
    # Calculate the cost of the dream home
    cost = cost_of_dream_home * portion_down_payment

    # The lowest annual rate to save up for a down payment in 3 years
    annual_rate = None

    # The main args for bisection search
    low = 0.0
    high = 1.0
    step = 0

    # Check if the initial deposit is enough to buy the dream home
    if initial_deposit >= cost - 100:
        return low, step
    else:
        # The main loop to calculate the lowest annual rate
        while high - low > 0.0001:
            step += 1
            mid = (low + high) / 2
            amount_saved = initial_deposit * (1 + mid / 12)**36 
            if abs(amount_saved - cost) <= 100:
                annual_rate = mid
                return annual_rate, step
            elif amount_saved < cost - 100:
                low = mid
            else:
                high = mid
        return annual_rate, 0

if __name__ == "__main__":
    # verb = input("Type a verb:")
    # print("I can " + verb + " better than you." )
    # print((verb + " ") * 5)
    # yearly_salary = float(input("Enter your yearly salary:"))
    # portion_saved = float(input("Enter the portion of your salary saved each month:"))
    # cost_of_dream_home = float(input("Enter the cost of your dream home:"))
    # semi_annual_raise = float(input("Enter the semi-annual raise of your salary:"))
    initial_deposit = float(input("Enter your initial deposit:"))
    print(f"The lowest r: {LowestrForHome(initial_deposit)[0]}, and the steps: {LowestrForHome(initial_deposit)[1]}")