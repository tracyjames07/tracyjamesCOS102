total = 50
def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function;_ local total: ", total)
    return total

sum(10, 20)
print("Outside the function; global total: ", total)