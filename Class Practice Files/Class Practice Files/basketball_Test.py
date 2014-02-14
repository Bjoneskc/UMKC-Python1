__author__ = 'bjones'

#Header Comments
import math

pointDifference = int(input("What is the point difference? "))
pointDifference -= 3

teamAhead = input("Does the team in the lead have the ball? ")
teamAhead = teamAhead.upper()

if teamAhead == "Y":
    pointDifference += 0.5
else:
    pointDifference -= 0.5

secondsLeft = int(input("How many seconds are left? "))

squareResult = math.pow(pointDifference, 2)


if squareResult > secondsLeft:
    print("The lead is safe")
else:
    print("The lead is in question")





