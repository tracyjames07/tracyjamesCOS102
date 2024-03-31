import math

print("Hello. Which program would you like to perform?")
print("a. The Roots of a Quadratic Equation Using the Quadratic Formula.")
print("b. The Roots of a Cubic Equation Using Cardano's Formula.")
print("Press 'A' for the 'Quadratic Function', and 'B' for the 'Cubic Function'.")

quadratic_function = "A"
cubic_function = "B"

function = input("Enter an option: ")

if function == "A":
    print("We'll be solving for the roots of quadratic equation.")
    print("The formula is [x = (-b ± √(b² - 4ac)) / (2a)].")
    print("You just need to enter values for 'a', 'b', and 'c'.")
    print("Please note that they must be decimal values.")

    a = float(input("Enter a value for 'a': "))
    b = float(input("Enter a value for 'b': "))
    c = float(input("Enter a value for 'c': "))

    quadratic_root_a = ((-b + (((b) ** 2.0) - (4 * a * c)) ** (1/2))) / (2 * a))