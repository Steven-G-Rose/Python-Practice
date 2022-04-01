This program was a lab from the Cisco Netacademy PCAP - Programming Essentials In Python course (3.1.1.11 LAB: Essentials of the if-else statement to be exact).

The only code that was provided to start with was the following:

    income = float(input("Enter the annual income: "))
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")

Here is the scenario:

"Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.

It should accept one floating-point value: the income.
Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

Look at the code in the editor - it only reads one input value and outputs a result, so you need to complete it with some smart calculations."

This exercise was actually quite simple. I was familiar with if and elif statements from previous research, so I was able to create it with minimal difficulty.

I added the while loop just because I like to make it possible to restart a program without having it completely close out.
