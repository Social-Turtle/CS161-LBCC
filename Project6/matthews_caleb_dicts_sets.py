#A sanbox to learn about dictionaries, sets, and their comprehensions
#Programmed by Caleb Matthews
#Instructed by Professor Joseph Jess

import copy

def user_string():
    while True:
        try:
            a = str(input("Input a string to add it to the dictionary. "))
        except ValueError:
            print("A string please!")
            continue
        else:
            return(a)
#function for user string input, validates evilness of input

def user_int():
    while True:
        try:
            a = int(input("Input an integer to add it to the dictionary. "))
        except ValueError:
            print("An integer please!")
            continue
        else:
            return(a)
#function for user integer input, validates evilness of input

def dict_to_list(component):
    output = list()
    for i in component:
        output.append(i)
    return output



def dict_func(dictionary):
    keys = list()
    values = list()
    for i in dictionary.keys():
        keys.append(i)
    for i in dictionary.values():
        values.append(i)
    for i in keys:
        num = len(keys[i])
        dictionary.update({keys[i]: num * values[i]}) 
    return dictionary
#since dictionaries can't be arranged, we'll multiply each value by the number of characters in the key

#create
sandbox_dict = {'Nugget': 'Chicken','Mac': 'Big', 'Coffee': 'Iced', 'McMuffin': 'Egg', 'Mind': 'Mega'}
print(type(sandbox_dict))
print(sandbox_dict)
print(len(sandbox_dict))

#add more data,
temp = { user_string(): user_int()}
sandbox_dict.update(temp)
print(sandbox_dict)

#change a value associated with a key in the dictionary,
sandbox_dict.update({'McMuffin': 'Sausage'})
print(sandbox_dict)

#remove data,
sandbox_dict.pop('Mind')
print(sandbox_dict)

test = sandbox_dict.keys
print(test)

#print(dict_func(sandbox_dict))


#Using dictionaries, show how we can:

#use a couple of methods (or your own functions) on dictionaries to accomplish some task
#Use Sets in some of the tasks similar to the above, but make special note in your code when we cannot perform a task exactly the same due to differences in the way Dictionary and Set objects behave.
#(Note: Yes, this can also be tricky, I know that there are several ways that they are similar and several ways in which they are different!)
#Use both Dictionaries and Sets as arguments to functions that you create, showing how they behave similarly and differently from each other (this also serves to demonstrate scope capabilities!), and remember that:
#parameters are local to the function,
#assignment operators change where a variable references (pointing to) memory (rather than altering the value at that variable's location in memory), but that mutable object references can be modified as a 
#side effect of the function,
#copying Dictionaries and Sets can be tricky with shallow copies, but sometimes that is exactly what we want!
#(you do not have to demonstrate a deep copy, a shallow copy is enough for this assignment),
#Show a simple Dictionary and a simple Set comprehension (maybe just a list of values that pass some conditional test or a simple zipping up of two different lists), 
#attempt to show more complicated Dictionary and Set comprehensions.

#Take a screenshot showing how you completed each numbered item above (with likely duplicates for the Sets being used instead of Dictionaries) 
#just be sure to number the items being displayed mention what the item is and a brief statement (maybe a sentence or two) explaining how that line of code meets the requirement listed.

#Note very well: The artifacts and explanations are as important in these later projects as the code itself!