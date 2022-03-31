#Written by Steven Rose on 3/31/2022

#Declare repeat variable
repeat = "y"

#Import math and set rounding to round 0.5 up
import math
def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

#Intro
print("This program evaluates the end time of a given event based on its start time and duration. \nEnsure that the time you enter is using a 24 hour clock and not a 12 hour clock. \nFor example, 1:00 PM on a 12 hour clock would be 13:00 on a 24 hour clock.\nTo explain how to use this program, we'll use an event that starts at 10:30 with a 30 minute duration as an example.\nTo enter the hour portion, enter \"10\".\nTo enter the minute portion, enter \"30\".\nTo enter the duration, enter \"30\".\nThe output would be \"11:00\" to indicate that this example event starting at 10:30 with a duration of 30 minutes would end at 11:00.\nTry using other times/durations below.\n")

#Creates loop so that program repeats once done
while True:
    #Input variables
    hour = int(input("Starting time (hour portion): "))
    mins = int(input("Starting time (minute portion): "))
    dura = int(input("Event duration (minutes): "))
    
#Calculate
    #Break down duration into hours perform addition
    end_hour = (hour + (dura / 60))
    #Fixes rounding issues when mins + dura < 60
    if (mins + dura) < 60:
        end_hour -= 0.1
    #Add minutes and duration modulo 60 to keep within limits of hour
    end_mins = (mins + dura) % 60
    
#Print results
    print(normal_round(end_hour), str(end_mins).zfill(2), sep=":")

#Ask user if they would like to try again
    repeat = input("Would you like to enter another time and duration? (y/n):")

#Continue loop if user wants to try again OR break loop if user does not want to try again
    if repeat == "y" or repeat =="Y":
        continue
    else:
        break
    
