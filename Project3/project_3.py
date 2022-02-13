#Week 3 Project

#Design:
#define library of words to draw from
#choose a word
#explain the game to user
#offer initial hint (len(word)?)
#begin loop while wordguessed == false:
# ask for user input
#      if input == hint:
#       input == character_in_word - list_of_inputs
# store input in list_of_inputs
# check word for character appearance(s) index and print
# grant user success message, press "enter" to quit.

#Design with new requirements:
#explain game to users, and what their roles are
#request and store input from player 1 as secret and input an integer
#clear player 1s input from terminal
#ask player two to guess if the integer is odd or even (change number of attempts)
#if player 2 is right, give random chances of 5-10 if wrong give 1-5
#ask player 2 for a letter, check validity, and output correct response
#display word so far... perhaps using index functions?
#after # of tries, print secret and list missing letters
#ask for an input to play again (define the entire program as a loopable function?)

from random import randrange

print("Hello, and welcome to piece-my-passcode! Today, you and your opponent will compete to the death!")
print("Well, maybe not to the death, but to guess a word! Player 1 will create a secret word that is 7 characters long,")
print("And player 2 will attempt to guess the word letter by letter. However, the attempts are limited.")
print("At the beginning of the game, Player 1 will also input an integer that is either 1 or 0, and if player two guesses their input correctly, they get more tries.")
print("However, there is some magic in the number of attempts you get, so lets home you're lucky!")

secret_word = str(input("Alright P1, input your seven-character word. Remember, only letters. No numbers or special characters!"))
secret_word = secret_word.lower()
secret_letters = return list(secret_word)
attempt_magnitude = int(input("Input either a 1 or a 0, whatever you think P2 won't choose!"))
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \nAlright P2, you're up!")
attempt_magnitude_guess = int(input("Alright P2, now is your turn to guess a 1 or a 0... What would P1 input?"))
attempt_potential = randrange(10)
if attempt_magnitude == attempt_magnitude_guess:
    attempt_potential = attempt_potential * 2

guessed = False
attempt_total = 0

while guessed == False and attempt_total <= attempt_potential:
    guessed_letter = str(input("P2, guess a letter!")).lower()
    guessed_letters_total += [guessed_letter] 
#I need some method for removing duplicates in a list...

#I also need a method to print each location in the secret_word that a guessed letter appears
#but I think I need a method to remove duplicates first...
    
    guessed_word = ""
    if guessed_word == secret_word:
        guessed = True
    attempt_total += 1

if guessed == True:
    print("Congratulations! You guessed the word!")
    else:
        print("Wah wah wah, you ran out of turns! :(")