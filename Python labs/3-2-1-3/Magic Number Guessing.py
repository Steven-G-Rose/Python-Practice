secret_number = 777
guessed_number = 1

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while guessed_number != secret_number:
    guessed_number = int(input("Type here to guess the number: "))
    if guessed_number != secret_number:
        print("Ha ha! You're stuck in my loop!")

print("Well done, muggle! You are free now.")
