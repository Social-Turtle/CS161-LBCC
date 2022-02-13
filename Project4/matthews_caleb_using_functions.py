#global definition of letters used, so it can be added to later
letters_used = list("")

#asks for word input and validate its evilness and output a good word
def word_input():
    while True:
        try:
            secret_word = str(input("Please input a seven-letter word: "))
            if len(secret_word) != 7:
                print("Ope! We need a seven letter word here! Please input a seven letter word! ")
                continue
        except ValueError:
            print("Ope! That isn't a word! Please try again. ")
            continue
        else:
            return(secret_word)
#asks for a letter input and validates its evilness
def letter_input():
    while True:
        try:
            letter_guess = str(input("Please input a letter: "))
            if len(letter_guess) != 1:
                print("Ope! That isn't one letter! Please try again! ")
                continue
        except ValueError:
            print("Ope! That isn't a letter! Please try again. ")
            continue
        else:
            return letter_guess

#count how many times the guessed letter appears and tell the user of their success or failure
def check_letter(letter):
    appearance_count = secret_word.count(letter)
    if appearance_count == 1:
        print(f"The secret word has {appearance_count} {letter}.")
    else:
        print(f"The secret word has {appearance_count} {letter}s.")

#determine which letters appear in the word and print underscores or letters accordingly
def vanna_white(secret_word,letters_used):
    current_string = ""
    #for each letter in the secret word
    for i in range(7):
        #go through each letter
        current_letter = secret_word[i]
        #see if the letter in the secret word = a letter used
        letter_present = any(element in secret_word for element in letters_used)
        #if so, add it to be printed
        if letter_present == True:
            current_string += current_letter
        #otherwise, add an underscore
        else:
            current_string += "_"
            i += 1

#Actual Program:
#define player 1's word
secret_word = word_input()

#begin loop (user gets 14 guess attempts)
for i in range(14):
    #define player 2's guess
    guessed = letter_input()
    #update list of attempted letters
    letters_used = letters_used.append(guessed)
    #inform user of their success/unsuccess
    print(check_letter(letter_input()))
    #update current guess-filled string
    vanna_white(secret_word,letters_used)
    #print guess
    print(current_string)
    if current_string == secret_word:
        print(f"Congratulations, you have successfully guessed the word! It was {secret_word}!")
        break
if current_string != secret_word:
    print(f"Oh no! It looks like you didn't manage to guess the word! It was {secret_word}...")
print("If you would like to play again, please press Fn F5!")