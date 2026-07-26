# walrus is creating variables during the time of execution.
# as shown below, using the := operator , it calculates the expression and assigning it to a variable

cupSizes = ["S","M","L","XL"]

if (varSelection := input("Please enter the required cup size : ").capitalize()) in cupSizes:
    print(f"Desired size {varSelection} is available")
else:
    print(f"No such cup is available.")