__author__ = 'bjones'
number = int(input("Enter a positive integer: "))
count = 0

print("Starting with number: ", number)
print("Sequence is: ", end='\n')

while number > 1:
    if number % 2:
        number = (number * 3) + 1
    else:
        number /= 2
    print(number, ",", end='\n')

    count += 1

else:
    print()
    print("Sequence is ", count, "numbers long")