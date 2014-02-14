#Header
import random

UserPot_int = 0
still_playing = True

#While the user is playing
#Be consistent with naming styles
while still_playing:
    #checking the initial input from the user and the program cannot continue unless this is correct
    while UserPot_int <= 0:
        UserPot_int = int(input("How much do you want in your pot: "))
        if UserPot_int <= 0:
            print("You must give an amount greater than 0: ")

#This section allows the game to start once user input is valid
    while UserPot_int > 0:
        wager_amount = 0
        # This section validates the wager amount and makes the user input a valid wager amount
        while wager_amount <= 0 or wager_amount > UserPot_int:
            wager_amount = int(input("How much do you want to wager? "))
            if wager_amount <= 0 or wager_amount > UserPot_int:
                print("Give wager amount greater than zero or less: ")

#Roll Dice both 1 and 2
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        #print the results of the die roll
        print("Die1 : ", die1, "Die2 : ", die2)

        #Calculation for rolling a 7
        if die1 + die2 == 7:
            print("You won ", wager_amount * 4)
            print("Pot: ", UserPot_int)
            UserPot_int += wager_amount * 4
        #Calcualtion for rolling anything else
        else:
            print("You Lost")
            print("Pot: ", UserPot_int)
            UserPot_int -= wager_amount
        print("Your Pot ", UserPot_int)

    #This section runs after the else that indicates the user has lost the game,
    # because we have excited the loop associated with the above section
    userAnswer = input("Do you want to play again? (Y)(Yes)").upper()
    #Used to load possible answers into a list
    if userAnswer in ["Y", "Yes"]:
        still_playing = True
    else:
        still_playing = False

print("Thanks for playing")



