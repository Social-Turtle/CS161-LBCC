import random
secret = random.randint(0,100)
#computer's secret value
guess = 101
#user guess input
print("Hello, welcome to the imitation game... Well actually, I'm not quite sure I'm ready for a Turing Test, but nonetheless, I need you to make a guess about me.")
print("I've selected an integer number between 0 and 100. You will have to guess (with the help of my hints) until you solve it!")

def verificator():
    guess = int(input("Make a guess... "))
    if guess > secret:
        print("Ope,",guess," is a little high.")
    if guess < secret:
        print(guess," is undershootin' it a touch.")
    if guess == secret:
        print("Congratulations, you guessed the number! It's,", guess,"!!!")
        quit()
#function to verify the users input as correct, high, or low. If user's input is correct, terminates function.

while guess != secret:
    verificator()
#calls guess verification function as long as the user has not guessed the secret