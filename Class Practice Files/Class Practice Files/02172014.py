#Search Algorithm to find the letter in a word
#Could this also be used to find a word in a grouping of words
#Could really be used for the hangman game


def find(word, letter):
    #starting from 0 will always in the last letter of the word
    #can this be done with a for loop
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    #return -1 if not found
    return -1

letter_to_search = input("Please enter a letter to search for: ")
if find("Jones", letter_to_search) == -1:
    print("Letter not found")
else:
    print("Found Letter: ", letter_to_search)

#Count the number of times a letter appears in a string
word = "bananna"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)
#Used this function to find a letter that is in two words

letter = "a"
def in_both(word1, word2):
    for letter in word1:
    if letter in word2:
    print letter