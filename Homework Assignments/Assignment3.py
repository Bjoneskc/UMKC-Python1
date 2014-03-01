##CS 101
##Program 3
##Brian L Jones
##blj2m2@mail.umkc.edu
##
##PROBLEM:
##
##
##ALGORITHM: I solved this problem as follows:
## 1. Read file from list of words
## 2. Randomly select word from file
## 3. Find out how many letters are in the selected word
## 4. Tell user how many letters are in their word
## 5. Display a row of dashes to show letters that have not been guessed
## 6. Ask user for their first guess
## 7. User is allowed to guess a single letter each turn and guessing the same letter more than
##    once does not have an impact
## 8. If the user guesses a letter that is in the word
##    a. Display how many times the letter is present
##    b. Update row of dashes with the guessed letter
##    c. Repeat process until the word is guessed or until the user guesses a letter that is
##    not in the word
## 9. If the user guess a letter that is not in the word
##    a. The user can guess an incorrect letter up to 7 times
##    b. Keep track of the number of incorrect guesses
##    c. If the user guesses an incorrect letter more than 7 times, display the hidden word
##    d. Ask if they would like to play again
## 10. If the word is guessed, display a congratulations message and ask if the user would like
##    to play again.
##    a. If yes, goto step 2
##ERROR HANDLING:
##    1. .
##
##
##OTHER COMMENTS:
##
##############################################################
#Import modules
import random

#Variables
gameState = "Active"
word = []
numberOfGuesses = 7
charIndex = 0
letterGuessed = ""
guessedLetters = []
displayWord = ""
lettersAvailable = ["A", "B", "C", "D", "E", "F", "G"
                    , "H", "I", "J", "K", "L", "M", "N",
                    "O", "P", "Q", "R", "S", "T", "U",
                    "V", "W", "X", "Y", "Z"]

# Import data from file
inputFile = open("dictionary.txt", "r").readlines()

#Read data in from file and append it into the word list
for line in inputFile:
    word.append(line)

while gameState == "Active":
    #Select a random word from the list and put it back into word as the new value
    word = random.choice(word).strip()
    displayWord = ("-" * len(word))

    # Game Introduction
    print("Welcome to Hangman\n")
    print("The word is", len(word), "letters long")
    print("You have ", numberOfGuesses, "guesses remaining")
    print("Word = ", displayWord)
    print("Guessed: ", letterGuessed)
    print("Available: ", end="")
    for char in lettersAvailable:
        print(char, end="")
    print()
    letterGuessed = input("==> ").upper()

    #Set to stop when the user runs out of guesses
    while numberOfGuesses > 0:
        if letterGuessed.isalpha():
            for index, letter in enumerate(word.upper()):
                if letter == letterGuessed:
                    guessedLetters.append(letterGuessed)
                    lettersAvailable.remove(letterGuessed.upper())
                    for charIndex in range(len(word)):
                        if word[charIndex].upper() == letterGuessed:
                            displayWord.replace(displayWord[word.index(letterGuessed)],letterGuessed.upper())
                        else:
                            displayWord += "-"
                    print("Word = ", end="")
                    for char in displayWord:
                        print(char, end="")
                    print("\nGuessed: ", letterGuessed.upper())
                    print("Available: ", end="")
                    for char in lettersAvailable:
                        print(char, end="")
                    print()
                    letterGuessed = input("==> ").upper()
            else:
                print("\nSorry that letter wasn't present")
                guessedLetters.append(letterGuessed)
                lettersAvailable.remove(letterGuessed.upper())
                numberOfGuesses -= 1
                print("You have ", numberOfGuesses, "guesses remaining")
                print("Word = ", displayWord)
                print("Guessed: ", letterGuessed)
                print("Available: ", end="")
                for char in lettersAvailable:
                    print(char, end="")
                print()
                letterGuessed = input("==> ").upper()
        else:
            print("Please enter a character to search")


    #When the game state changes the game is over
    gameState = "Completed"

print("Game Over\nThe word was", word)