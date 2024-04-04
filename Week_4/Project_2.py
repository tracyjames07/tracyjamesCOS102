print("IZFIN TECHNOLOGY'S ANNUAL TAX REVENUE (ATR) DEVELOPER")

print("\n")

print("Welcome to the annual tax revenue (ATR) developer.")
print("This helps us generate a proper revenue for you.")
print("Do ensure you input the proper values.")

print("\n")

work_experience = int(input("Enter your years of experience: "))
age = int(input("Enter your age: "))

if work_experience >= 25 and age >= 55:
    print("Your annual tax revenue (ATR) is N5,600,000.")

elif work_experience >= 20 and age >= 45:
    print("Your annual tax revenue (ATR) is N4,480,000.")

elif work_experience > 10 and age >= 35:
    print("Your annual tax revenue (ATR) is N1,500,000.")

elif work_experience < 10 and age < 35:
    print("Your annual tax revenue (ATR) is N550,000.")

else:
    print("You don't qualify for this program.")