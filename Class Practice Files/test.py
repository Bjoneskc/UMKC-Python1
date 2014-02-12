__author__ = 'bjones'

# Put complete header at the top of the file

#get input from user
#Get number of touchdowns
#Get number of field goals
#Get number of safeties
#Calculate total points

#calculate total touch down point, number of touchdown * 7
#same for the other numbers

#future code - need to check for alpha characters so you don't get an error

touchdowns_str = input("How many touch downs were scored! ")
fieldgoals_str = input("How man field goals were scored! ")
safeties_str = input("How many safeties! ")

totalTouchDowns_int = int(touchdowns_str) * 7
totalFieldGoals_int = int(fieldgoals_str) * 3
totalSafeties_int = int(safeties_str) * 2

totalScore = totalTouchDowns_int + totalFieldGoals_int + totalSafeties_int

print("Total Score is: ", totalScore)










