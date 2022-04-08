c0 = int(input("Enter number: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0 and c0 != 1:
        c0 //= 2
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("steps = ", steps)
