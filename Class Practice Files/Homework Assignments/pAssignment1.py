##CS 101
##Program 1
##Brian L Jones
##blj2m2@mail.umkc.edu
##Creation Date: 01/30/2014
##Date Due: 02/02/2014
##
##PROBLEM: Write them a Python program that gets
## the number of upper, lower, and corner cabinets
## from the user, then computes the cutting, sanding,
## finishing and total hours.
##
##ALGORITHM: I solved this problem as follows:
##    1. Capture input for upper cabinets
##    2. Capture input for lower cabinets
##    3. Capture input for corner cabinets
##    4. Print a blank space to match example
##    5. Calculate totals for upper Cabinets, lower Cabinets, corner Cabinets and total Labor Hours
##    6. Print individual totals, then total labor costs
##
##ERROR HANDLING:
##    1. No error handling for this first program
##
##OTHER COMMENTS:
##    No additional comments for this first program
##############################################################

numUpperCabinets = int(input("Enter the number of upper cabinets: "))
numLowerCabinets = int(input("Enter the number of lower cabinets: "))
numCornerCabinets = int(input("Enter the number of corner cabinets: "))
print()

totalCuttingHrs = (numUpperCabinets * 1.2) + (numLowerCabinets * 1.5) + (numCornerCabinets * 1.9)
totalSandingHrs = (numUpperCabinets * 2.4) + (numLowerCabinets * 1.8) + (numCornerCabinets * 1.2)
totalFinishingHrs = (numUpperCabinets * 3.4) + (numLowerCabinets * 2.5) + (numCornerCabinets * 1.5)

totalLaborHrs = totalCuttingHrs + totalSandingHrs + totalFinishingHrs

print("Total cutting hours: ", totalCuttingHrs)
print("Total sanding hours ", totalSandingHrs)
print("Total finishing hours: ", totalFinishingHrs)
print("Total labor hours: ", totalLaborHrs)