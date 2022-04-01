repeat = "y"

while True:

    income = float(input("Enter the annual income: "))

    if income <= 85528:
        tax = income * 0.18 - 556.02
    elif income >= 85528:
        tax = 14839.02 + 0.32 * (income - 85528)
    if tax <= 0:
        tax = 0
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")

    repeat = input("Would you like to enter another income? (y/n): ")
    
    if repeat == "y" or repeat =="Y":
        continue
    else:
        break
