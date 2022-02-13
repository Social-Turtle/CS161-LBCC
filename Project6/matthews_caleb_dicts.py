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
    output = []
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
