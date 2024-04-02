import math

print("Hello. Which program would you like to perform?")
print("1. The Roots of a Quadratic Equation Using the Quadratic Formula.")
print("2. The Roots of a Cubic Equation Using Cardano's Formula.")
print("Press '1' for the 'Quadratic Function', and '2' for the 'Cubic Function'.")

function = int(input("Enter an option: "))
print(function)

if function == 1:

    print("We'll be solving for the roots of a quadratic equation.")
    print("The formula is [x = (-b ± √(b² - 4ac)) / (2a)].")
    print("You just need to enter values for 'a', 'b', and 'c'.")
    print("Please note that they must be decimal values.")

    a = float(input("Enter a value for 'a': "))
    b = float(input("Enter a value for 'b': "))
    c = float(input("Enter a value for 'c': "))

    quadratic_root_a = (-b + (((b ** 2.0) - (4 * a * c)) ** (1/2))) / (2 * a)
    quadratic_root_b = (-b - (((b ** 2.0) - (4 * a * c)) ** (1/2))) / (2 * a)

    print(f"The roots of the given quadratic equation are {quadratic_root_a} and {quadratic_root_b}.")

elif function == 2:

    print("We'll be solving for the roots of a cubic equation using Cardano's formula.")
