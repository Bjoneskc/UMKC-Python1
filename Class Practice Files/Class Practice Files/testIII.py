__author__ = 'bjones'
percent_float = float(input("What is your percentage: "))

if 90 <= percent_float < 100:
    print("You received an A")
elif 80 <= percent_float < 90:
    print("You received a B")
elif 70 <= percent_float < 80:
    print("You received a C")
elif 60 <= percent_float < 70:
    print("You received a D")
else:
    print("You did not pass")