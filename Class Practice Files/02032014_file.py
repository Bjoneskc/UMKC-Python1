__author__ = 'bjones'
#Used to bring in the import module
import random
user_input = 15
rabbit_hp = 15
flight_or_run = "F"

while user_input > 0 or rabbit_hp > 0 and flight_or_run != "R":
    rabbit_hp -= random.randint(1, 4)
    user_input -= random.randint(1, 4)
    print("My hp: ", user_input, "\tRabbit", rabbit_hp)
    flight_or_run = input("Do you want to flight ir run? (F) (R)").upper()

    if flight_or_run == "R":
        #could use break to simulate the same structure as a case statement
        break
# else will execute after the while runs
else:
    if user_input <= 0:
        print("You died")
    if rabbit_hp <= 0:
        print("The rabbit Died")
    print("Encounter is over")

    print('Outside of the loop here')