blocks = int(input("Enter the number of blocks: "))
height = 0
layers = 1

while layers <= blocks:
    height += 1
    blocks -= 1
    layers += 1

print("The height of the pyramid:", height)
