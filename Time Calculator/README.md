This program was a lab from the Cisco Netacademy PCAP - Programming Essentials In Python course (2.6.1.11 LAB: Operators and expressions to be exact).

The only bit of code that was provided to start the lab was the declaration of the hour, mins, and dura variables.

The scenario from the curriculum is the following:

"Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console. For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16. Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data. Test your code carefully. Hint: using the % operator may be the key to success."

The hint about using the modulus operator helped out a ton with this lab. 

I started with declaring the end_hour variable which entailed breaking down the dura variable into hours so that I could add the hours and minutes together.

I then declared the end_mins variable to add the mins and dura variables together and included modulus 60 so that it would keep the results within the confines of 60 minutes as it wouldn't make sense for the minutes on a clock to be over 59. Notice how I didn't include the modulus on the end_hour variable yet? More on that later!

Next, I used print to print the results with the correct formatting.

I noticed that at this point that it was printing the time, but since I was adding fractions of hours together, the end_hour variable came out as a float with multiple decimal points. I first attempted to fix this by using round() to round the number, but I noticed that the round function would often round down when end_hour = hour + 0.5. This led to me Googling how to round up in Python, and I came across a post from fedor2612 on https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers in which they imported the math module and created a function to round up if the float was 0.5 or higher. This seemed to do the trick, but I then ran into strange behavior in which if mins + dura >= 60, the end_hour output was wrong more often than not.

After much trial and error, I created the following code to subtract 0.1 from end_hour if mins + dura < 60, and it seems to have resolved my issue.

    if (mins + dura) < 60:
        end_hour -= 0.1
        
 What this does is correct the rounding up issue when mins + dura < 60. It took hours of trying multiple solutions until I finally came up with this small bit of code that seemingly fixed my issues. 
 
 But wait...remember earlier when I mentioned the modulus on the end_hour variable?
 
 I noticed that when I would enter large numbers for the dura variable that my end_hour variable would reach over 24 which doesn't make sense due to the fact that there are only 24 hours in a day! This was fortunately a quick fix. I threw a "% 24" at the end of my end_hour variable declaration and that fixed that issue as well.
 
With the "meat" of the program done, I started spicing it up a little bit. I Googled around and discovered "while loops" which led me to put my calculations in a loop and ask the user if they would like to enter another one. I cleaned up the results and discovered the zfill function to ensure that the minutes place always has two  digits. I also experimented with "if else" statements to create the logic for asking if the user wants to repeat the program or close it out.

Overall, I went above and beyond what the lab asked for, but I'm sure glad I spent so much time doing so because it led to a fun and organic learning experience. It taught me so much about Python in general and really made me realize that I have a passion for programming that I didn't even know I had!

Note that this program does not include any error handling yet as it is something I have not covered in my studies yet.

Here is some test data from the lab to input yourself if you'd like:


Sample input:

12

17

59

Expected output: 13:16


Sample input:

23

58

642

Expected output: 10:40


Sample input:

0

1

2939

Expected output: 1:0
