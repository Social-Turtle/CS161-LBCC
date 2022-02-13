import driver
import random
from operator import attrgetter
#function to sort lists by object attribute

print('\n\n\nHello, and welcome back to everyone\'s favorite CS161 game show, Guesserator 4000!')
print(f'My name is... uhh, what is my name again?')
#intro/description

name = driver.input_string('Please remind me of my name, or if you want me to come up with my own, just hit the \'Enter\' key! ')
if name == '':
  name = 'Ted Bilderbund'
#allow player to input name for announcer, or leave it be
print(f'Ohhhh that\'s right! My name is {name}!')
print('And what\'s that old catchphrase of mine?')
catchphrase = driver.input_string('Please remind me of my catchphrase! ')
experience = random.randrange(42)
print(f'\nWell, I reckon that after {experience} years of hosting, I\'m startin\' ta become an old loon!')
print('But nevermind that, we\'re here to play Guesserator 4000!')
announcer = driver.announcer(name,experience,random.randrange(10),random.randrange(10),catchphrase)
#develop announcer attributes

player_list = []
player_list.append(driver.player(driver.input_string('By the way, what is your name? '),0,True))
round_count = driver.input_integer('\nHow many rounds would you like to play? ')
for i in range(driver.input_integer('\nHow many opponents would you like to play? ')):
  #i+2 is used so that the user can be player one.
  name = driver.input_string(f"\nPlease name opponent {i+1}! ")
  sentience = input('If you would like this player to be user controlled, enter \"1\". Otherwise, press any key to continue. ')
  if sentience == '1':
    sentience = True
  else:
    sentience = False
  player_list.append(driver.player(name,0,sentience))
#ask user to input names for their opponents

print(f'\n\nWell {announcer.catchphrase}! It looks like we are just about ready to begin!')
print('Let\'s do a quick roll call for our participants in today\'s game!')
for i in range(len(player_list)):
  print(f'Please welcome {player_list[i].name}!')
print(f'\nNow without further ado, let\'s begin the game! {announcer.catchphrase}!')
#give players an idea of who all is in the game

for i in range(round_count):
  #repeat for each phrase
  guess_set = set({})
  printout = ''
  turn = 0
  all_chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
  current_phrase = driver.phrase_library[random.randrange(12)]
  announcer.phrase_intro(current_phrase.theme,current_phrase.hint)
  print(driver.print_guess(current_phrase.text,'',guess_set))
  #print blank output for initial guess
  while printout != current_phrase.text:
    #for EACH TURN
    current_turn = player_list[turn]
    if current_turn.real == True:
      print(f'\n{current_turn.name}\'s turn!')
      guess = driver.input_letter('Please guess a single letter that has not yet been guessed: ', all_chars, guess_set)
    #if the player is real, let them pick a letter
    if current_turn.real == False:
      guess = random.choice(tuple(all_chars - guess_set))
    print(f'\n{current_turn.name} guessed {guess}!')
    #if the player is not real, generate a letter
    appearances = driver.appearance_count(guess,current_phrase.text)
    announcer.announce_count(appearances,guess)
    announcer.speak(appearances,current_turn.score,current_turn.name)
    printout = driver.print_guess(current_phrase.text,guess,guess_set)
    print(printout)
    #printout variable is not directly placed in print function so it can communicate to loop condition
    current_turn.score += appearances * 5
    turn += 1
    if turn == len(player_list):
      turn = 0
  if (round_count - (i+1)) == 1:
    print(f'{announcer.catchphrase}! You completed the phrase! There is 1 more round to go! Time to focus!\n')
  else:
    print(f'{announcer.catchphrase}! You completed the phrase! There are {round_count-(i+1)} rounds to go!\n')

player_list.sort(key=attrgetter('score'),reverse=True)
print(f'\n\nAnd that\'s the game! {announcer.catchphrase} was that a great competition!')
print(f'In my {announcer.experience} years of hosting, I have never seen such a great game!')
print('Now, there\'s only one thing left for me to do... announce the victor!')
print(f'With an astonishing score of {player_list[0].score} points, today\'s Guesserator 4000 champion is...')
print('\n*drumroll...*\n')
print(f'***{player_list[0].name}***!!!!!!\n\n\n')
print(player_list)
print('Congratulations everyone for a game well played! We\'ll see you next time right here on Guesserator 4000!')
print(f'Until then folks, {announcer.catchphrase} and goodnight!')
input('Press any key to exit.')