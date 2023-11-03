### Setup Section ###

#  it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is 
    #in the secret word AT ALL or not
    if letter in actual:
      
      


      # If the letter is in the secret word, is it also AT THE 
    #CURRENT INDEX in the secret word?
      if(letter == actual[index]):
        

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point 
    #in the code that it's still used in the secret word somewhere...
      else:
        printColorfulLetter(letter, True, False)

        # ...so we'll print it out with a yellow background

    # ...but if the letter is not in the word at all...
    else:
      printColorfulLetter(letter, False, False)
      # ...print it out with a red background

    # just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# Write a Function that takes in a six-lettered word from the user
def getUserGuess():
  guess = input("Enter a 6 letter word: ")
  guess = guess.upper()
  count = 0
  while len(guess) != 6:
    guess = input("Enter a 6 letter word: ")
    guess = guess.upper()
  if (len(guess) == 6): 
    
    return guess
  
      


### Main Program ###


#Introduction to the Game
print("Welcome to Word Play!")
print("======================")
print("You have 6 tries to get the word correct")
print("The word is 6 CHARACTERS LONG, and you must enter a guess of this length")
print("If a letter is in the correct palce, it will be green")
print("If a letter is in the word, but NOT in the correct place, it will be yellow")
print("If the letter is NOT in the word, it will be red")
print()

#Secret Word
actual = "TARGET"
#user enters a guess
guess = ""
enteredGuess = getUserGuess()
print(enteredGuess)

printGuessAccuracy(enteredGuess, actual)
count = 0
while enteredGuess != actual and count <5:
  print()
  enteredGuess = getUserGuess()
  printGuessAccuracy(enteredGuess, actual)
  print(enteredGuess)
  count +=1

#DISPLAY WIN or LOSE Message
if enteredGuess == actual:
  print()
  print(f"You're Right! It is {actual}")

else:
  print(f"Sorry, the correct answer was {actual}. Try again tomorrow.")

  


