#A sandbox to learn about lists and tuples
#Programmed by Caleb Matthews
#Instructed by Professor Joseph Jess
import copy

def user_string():
    while True:
        try:
            a = str(input("Input a string to add it to the list. "))
        except ValueError:
            print("A string please!")
            continue
        else:
            return(a)
#function for user string input, validates evilness of input

def user_int():
    while True:
        try:
            a = int(input("Input an integer to add it to the list. "))
        except ValueError:
            print("An integer please!")
            continue
        else:
            return(a)
#function for user integer input, validates evilness of input

def is_string(list):
    cell_count = len(list)
    for i in range(cell_count):
        if type(list[i]) == str:
            list[i] = True
        else:
            list[i] = False
    return list
#replaces each element of a list with a statement of true or false depending if it is a string or not

def list_mult(list, coefficient):
    new_list = []
    for ele in list:
        try:
            initial_value = int(ele)
            ele = initial_value * coefficient
            new_list.append(ele)
        except:
            new_list.append(ele)
        finally:
            pass
    return new_list
#multiply all integer elements of a list by the given coefficient, strings remain untouched

def tuple_is_string(tuple):
    tuple_func_list = []
    for i in range(len(tuple)):
        try:
            a = int(tuple[i])
            tuple_func_list += ['integer']
        except:
            a = str('string')
            tuple_func_list += ['string']
        finally:
            pass
    return(tuple(tuple_func_list))

#outputs a tuple expressing a statement of true or false depending if the equivalent element is a string or not
print("Do we have a list yet?")
sandbox_list = 'Is this a list yet? 4 15 32'
print(sandbox_list)
#no, just because I named it sandbox_list doesn't mean it isn't a string

print('Clearly, this is not a list. \n\n\nWhat is it then?')
print(f'It\'s a {type(sandbox_list)}!')

print('\n\n However, if we use the split function, we can divide this string into a list!')
sandbox_list = list(sandbox_list.split())
print(sandbox_list)
#however, if I split it, and place it into a list format, it will form a list!

print('\n\n Wow! That\'s pretty cool! Let\'s add another string element to this list!')
sandbox_list += [user_string()]
print(sandbox_list)
#add user data to the end of the list

print("\n\nNow let's change the word \"a\" to something else!")
sandbox_list[2] = str(user_string())
print(sandbox_list)
#use user data to replace an element of the list

print("\n\nNow let's remove the second element of our list!")
sandbox_list.remove(sandbox_list[1])
print(sandbox_list)
#remove a data element

print("\n\nNext, we will print only element 3 from our list!")
print(sandbox_list[2])
#access a specifically indexed element from the list

print("\n\nNow, let's multiply the integers in our list, by any number that you would like!")
sandbox_list = list_mult(sandbox_list, user_int())
print(sandbox_list)

print("\n\nLet's check if the elements of our list are strings or not!")
string_check = copy.deepcopy(sandbox_list)
is_string(string_check)
print(string_check)

print("\n\nNow, let's try something more complex!")
print("If the element is an integer, we will check to see if it is odd.")
print("If the element is a string, we will check to see if it contains the letter 'e'.")

print(sandbox_list)
for i in range(len(sandbox_list)):
    try:
        a = int(sandbox_list[i])
        if a%2 == 0:
            sandbox_list[i] = 'Even'
        else:
            sandbox_list[i] = 'Odd'
    except:
        a = str(sandbox_list[i])
        if a.find('e') >= 0:
            sandbox_list[i] = 'E Present'
        if a.find('e') == -1:
            sandbox_list[i] = 'E Not Present'
print(sandbox_list)

print('\n\nNow let\'s begin the same process, but with tuples, to see what we can do!')
sandbox_tuple = 'Is this a tuple yet? 4 15 32'
print(sandbox_tuple)
#no, just because I named it sandbox_tuple doesn't mean it isn't a string

print('Clearly, this is not a tuple. \n\n\nWhat is it then?')
print(f'It\'s a {type(sandbox_tuple)}!')

print('\n\nHowever, if we use the split function, we can divide this string into a tuple!')
sandbox_tuple = tuple(sandbox_tuple.split())
print(sandbox_tuple)
print(type(sandbox_tuple))

print('\n\nNow, let\'s try adding a string to our tuple!')
sandbox_tuple += (user_string(),)
print(sandbox_tuple)

print('\n\nNow, we will replace the word \'attempt\' with an integer!')
print('Because tuples are immutable, we will have to convert this tuple into a list, and then back into a tuple!')
sandbox_tuple = list(sandbox_tuple)
sandbox_tuple[5] = user_int()
sandbox_tuple = tuple(sandbox_tuple)
print(sandbox_tuple)
print(type(sandbox_tuple))

print('\n\nNext, we will use the same method to remove the fourth element from this tuple!')
sandbox_tuple = list(sandbox_tuple)
sandbox_tuple.remove(sandbox_tuple[3])
sandbox_tuple = tuple(sandbox_tuple)
print(sandbox_tuple)

print('\n\nAnd now, we shall print a single element from our tuple. We\'ll do the seventh element!')
print(sandbox_tuple[6])

print("\n\nLet's check if the elements of our tuple are strings or not!")
print(tuple_is_string(sandbox_tuple))