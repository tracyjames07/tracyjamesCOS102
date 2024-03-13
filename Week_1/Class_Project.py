print("The formula for Simple Interest is: A = P(1 + (R/100)T).")
print("A = Amount.")
print("R = Rate.")
print("P = Principal.")
print("T = Time.")
print("Let's try an example.")

rate = int(input("Enter a value for rate: "))
principal = int(input("Enter a value for principal: "))
time = int(input("Enter a value for time: "))

amount = principal * ((1 + (rate / 100)) * time)

print("Simple Interest is equal to " + str(amount) + ".")



print("The formula for Compound Interest is: (A = P(1 + (R/n))^(nt)) - P.")
print("A = Amount.")
print("P = Principal.")
print("R = Rate.")
print("n = Number of times interest is compounded per year.")
print("t = Time.")

n = int(input("Enter a value for 'n': "))

compound_interest = (principal * (1 + (rate / n)) ** (n * time)) - principal

print("Compound Interest is equal to " + str(compound_interest) + ".")



print("The formula for an Annuity Plan is A = (PMT) * [(1 + (R / n)^(n * t) - 1] / (R / n).")
print("PMT = Payment per period.")

pmt = int(input("Enter a value for PMT: "))

annuity_plan = pmt * ((1 + (rate / n)) ** (n * time) - 1) / (rate / n)

print("Annuity Plan is equal to " + str(annuity_plan) + ".")