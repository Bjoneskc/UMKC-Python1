__author__ = 'bjones'

#This code is useful for the game pig simulation.
# You will want to create a loop within a loop or use a function to process the loop information
user_str = input("Give us the perfect number to test")
max_int = int(user_str)

user_int = int(user_str)
numberToTest = 1
While numberToTest <= max_int:

    counter = 1
    sum_int = 0

    while counter < user_int:
        #test to see if user_int is divisible by zero
        if user_int % counter == 0:
            sum_int += counter
        counter += 1

if sum_int == user_int:
    print(user_int, "is a perfect number")
else:
    print(user_int, "is not a perfect number")