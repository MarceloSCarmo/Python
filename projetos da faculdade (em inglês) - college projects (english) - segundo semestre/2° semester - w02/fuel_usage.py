
"""Write a Python program that asks the user for three numbers:

A starting odometer value in miles
An ending odometer value in miles
An amount of fuel in gallons
Your program must calculate and print fuel efficiency in both miles per gallon and liters per 100 kilometers.
Your program must have three functions named as follows:

main
miles_per_gallon
lp100k_from_mpg
All user input and printing must be in the main function. In other words, 
the miles_per_gallon and lp100k_from_mpg functions must not call the the input or print functions."""



import math

def main():
    starting_odometer = float(input(f"What's the starting odometer value in miles? "))
    ending_odometer = float(input(f"What's the ending odometer value in miles? "))
    amount_of_fuel = float(input(f"What's the amount of fuel in gallons? "))
    
    # This fuction calculates the fuel efficiency in U.S.
    mpg = miles_per_gallon(starting_odometer, ending_odometer, amount_of_fuel)

    # This fuction calculates the fuel efficiency in other cuntries. 
    lp100k = lp100k_from_mpg(ending_odometer, mpg)

    print(f"\nFuel efficiency for gasoline powered vehicles is: {mpg:.2f} miles per gallon.")
    print(f"\nFuel efficiency for gasoline powered vehicles is: {lp100k:.2f} liters per 100 kilometers.\n")

def miles_per_gallon(starting_odometer, ending_odometer, amount_of_fuel):
    mpg = (ending_odometer - starting_odometer) / amount_of_fuel

    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg

    return lp100k

main()