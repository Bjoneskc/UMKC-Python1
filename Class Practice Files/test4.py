__author__ = 'bjones'

# simple for
# find the sum of the numbers from 1 to 100

the_sum = 0

for number in range(1, 101):
    the_sum += number
    print(the_sum)

# print is outside of the for loop
print()
print("Sum is: ", the_sum)