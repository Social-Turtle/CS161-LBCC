#driver file for CS161 Final Project
#Written by Caleb Matthews
#Instructed by Joseph Jess
from os import name
import random

def input_string(statement):
    while True:
        try:
            a = str(input(statement)).lower()
        except ValueError:
            print("A string please!")
            continue
        else:
            return(a)
#function for user string input, validates evilness of input

def input_integer(statement):
    while True:
        try:
            a = int(input(statement))
        except ValueError:
            print("An integer please!")
            continue
        else:
            return(a)
#function for user integer input, validates evilness of input

def input_letter(statement,check_set, guess_set):
    while True:
        try:
            a = str(input(statement)).lower()
        except ValueError:
            print("A string please!")
            continue
        if (len(a) == 1) and (a in check_set) and (a not in guess_set):
            return a
        else:
            print('That is not a single letter that has not been guessed!')
            continue
#a modification of input_string specifically for monocharacter arabic input

def print_guess(phrase,guess,set):
    printout = ''
    set.add(guess)
    for i in range(len(phrase)):
        if phrase[i] in set:
            printout += phrase[i]
        elif phrase[i] == ' ':
            printout += ' '
        else:
            printout += '_'
    return printout
#function to printout the _blocked version of the phrase for users

def appearance_count(guess, phrase):
    count = 0
    for i in range(len(phrase)):
        if guess == phrase[i]:
            count += 1
    return count
#function to count number of a letter's appearances in the phrase

class player:
    def __init__(self, name = 'Player', score = 0, real = False):
        self.name = name
        self.score = score
        self.real = real
    def __repr__(self):
        return self.name + ": " + str(self.score)

class phrase:
    def __init__(self, text, hint, theme):
        self.text = text
        self.length = len(self.text)
        self.hint = hint
        self.theme = theme
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text

class announcer:
    def __init__(self, name = "Ted Bilderbund", experience = 22, meanness = 10, talkativeness = 10, catchphrase = ''):
        self.name = name
        self.experience = experience
        self.meanness = meanness
        self.talkativeness = talkativeness
        self.catchphrase = catchphrase
    def __str__(self):
        return str(self.catchphrase)
    def phrase_intro(self,theme, hint):
        print(f'The category is {theme}')
        print(f'The hint for this phrase is {hint}')
    def announce_count(self, count, guess):
        if count == 0:
            print(f'There are no \'{guess}\'s.')
        elif count == 1:
            print(f'There is 1 \'{guess}\'.')
        else:
            print(f'There are {count} \'{guess}\'s.')
    def speak(self, appearances, score, name):
        
        nspeak1 = f'Wow, that certainly wasn\'t what I\'d consider a winning performance.'
        nspeak2 = f'Folks, it must be {name}\'s first time playing, let\'s cut them some slack.'
        nspeak3 = f'You only have {score} points right now? My grandmother could do better!'
        nspeak4 = f'Imagine being so bad that you guess a letter and it only shows up {appearances} times.'
        nspeak5 = f'At this point, if you only have {score} points, it would be shocking if you didn\'t lose.'
        
        nice_quotes = (nspeak1,nspeak2,nspeak3,nspeak4,nspeak5)
        
        mspeak1 = f'What an excellent guess!'
        mspeak2 = f'{self.catchphrase}! {name} has some serious skills!'
        mspeak3 = f'With {score} points, my bet is on {name}'
        mspeak4 = f'At this point, is there any way {name} could not win?'
        mspeak5 = f'{self.catchphrase}'
        
        mean_quotes = (mspeak1,mspeak2,mspeak3,mspeak4,mspeak5)
        
        a = random.randrange(10)
        if a <= self.talkativeness:
            a = random.randrange(10)
            if a <= self.meanness:
                print(nice_quotes[(random.randrange(len(nice_quotes)))])
                pass
            else:
                print(mean_quotes[(random.randrange(len(nice_quotes)))])

a = phrase('i am your father','surprise','movie quotes')
b = phrase('clever girl', 'appreciation','movie quotes')
c = phrase('a simple spell but quite unbreakable', 'warning','movie quotes')
d = phrase('shaken not stirred','order','movie quotes')
e = phrase('eiffel tower', 'ratatoullie', 'architecture')
f = phrase('notre dame', 'fire', 'architecture')
g = phrase('great wall of china', 'ancient', 'architecture')
h = phrase('a human readable essay', 'what is a program?', 'cs161')
i = phrase('often and thoroughly', 'test your code...', 'cs161')
j = phrase('if it was hard to write it is hard to read', 'write a comment', 'cs161')
k = phrase('visual studio code','where was this written?', 'cs161')
l = phrase('sufficient care and propulsion', 'the requirements for pigs to fly','cs161')
m = phrase('pyramids of giza', 'huge', 'architecture')

phrase_library = (a,b,c,d,e,f,g,h,i,j,k,l,m)
