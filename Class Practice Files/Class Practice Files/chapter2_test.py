__author__ = 'bjones'

#had to convert to int before using the string value in bool expression
tenure = int(input("How long has employee been here: "))

if tenure >= 20:
    print("Give a 20% raise")
#this is == to else if
elif tenure >= 10:
    print("give a 10% raise")
else:
    print("He needs to work longer")

print("Finish")


