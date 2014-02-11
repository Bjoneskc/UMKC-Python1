##CS 101
##Program 2
##Brian L Jones
##blj2m2@mail.umkc.edu
##Creation Date: 02/10/2014
##Date Due: 02/16/2014
##
##PROBLEM: Pig is a simple two player dice game, played with one die. The first player to reach or surpass
##50 is the winner. Each player takes a turn rolling the dice. They add to the pot with each roll,
##having to decide to roll again and increase the pot, or cash out. The risk being they could lose
##the amount they’ve accumulated into the pot.
##
##ALGORITHM: I solved this problem as follows:
##    1. Display current score for person and computer
##    2. Request the person hit enter to continue at the start of the turn
##    3. If the user rolls a 1:
##      1. Score set to zero for user
##      2. Round Pot set to zero for user
##      3. Message indicates to the user that “1 = Bust”
##      4. Display current score for user and computer
##      5. turn switches to the other player
##    4. If the the user rolls a 2-6:
##      1. Add the number of the roll to the users “round” pot and increase the users pot for the current
##    game
##      2. Display the die roll, new pot amount and provide option to roll again or hold
##          1. Accept r,R,h,H as valid input
##          2. Do not allow net round to continue unless input is valid at step 3
##          3. If hold is chosen as an option, display the user score and computer score
##    5. The computer will end its turn if the round pot is 20 or greater
##    6. Check the computers score at the beginning of its turn to see if the computer's score is 50 or
##      greater. If the computer score if 50 or greater, select hold for the computer to exit the game as
##      the winner.
##    7. Once a players score is 50 or greater, that player has won.
##      1. Output score totals, and winner information
##      2. Provide option to play again in the form of Y or N
##      3. only accept y,Y,n,N values to play the game again
##    8. Keep track of the last player that rolled in the game and select the other player to go first for the
##      next game.
##
##ERROR HANDLING:
##    1. check input values to make sure they qualify to allow program execution to continue
##
##OTHER COMMENTS:
##    I am going to go ahead and add the score to the display along with with the Die
##    and the Pot. I don't really gamble but it seems that I would want to know what my score is
##    before I decide if I want to roll again. I only find out by selecting h as an option which makes
##    me forfeit a turn.
##############################################################
#import needed modules
import random

#Set game variables
userScore = 0
userRoundPot = 0
computerScore = 0
computerRoundPot = 0

# the die variable contains a random number from 1 to 6
die = random.randint(1, 6)

while userScore <= 50 or computerScore <= 50:




