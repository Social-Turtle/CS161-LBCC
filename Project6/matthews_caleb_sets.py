import copy
#a feature we  use later as the max function destroys the set in process of running
import random
#a feature we use later to randomly assign positions to a group of people

def user_string():
    while True:
        try:
            a = str(input("Input a string to add it to the set. "))
        except ValueError:
            print("A string please!")
            continue
        else:
            return(a)
#function for user string input, validates evilness of input

def user_int():
    while True:
        try:
            a = int(input("Input an integer to add it to the set. "))
        except ValueError:
            print("An integer please!")
            continue
        else:
            return(a)
#function for user integer input, validates evilness of input

#define input functions

def set_max(set):
    compare_val = 0
    #the value we will check our current element against, starts at 0
    length = len(set)
    #a variable to define the length of our set for the for loop. It cannot use var in set because the length of set repeatedly changes
    for i in range(length):
        ele = set.pop()
        try:
            int(ele)
            if ele >= compare_val:
                compare_val = ele
            #if the element is greater than 0 or the previous element, store it and throw out the old data
        except ValueError:
            continue
        finally:
            continue
    print(f"{compare_val} is the greatest integer in the set!")


sandbox_set = {1,2,3,4,5,6,7,8,9, 'chicken', 'steak', 'ninjas', 8.03}
print(sandbox_set)
print(type(sandbox_set))
#demonstrate that we have a set

print('Now, we will add some data of a new type to our set!')
sandbox_set.add(user_string())
print(sandbox_set)

#since we can't update a body of different things, and change one to another, as there is not data to define them as a change,
#in this case we will resort to removing one element, and simply adding another to give the illusion of changing data
print('Next, we shall remove an element')
sandbox_set.remove(2)
print(sandbox_set)

sandbox_set.add(user_int())
print(sandbox_set)

temp_set = sandbox_set.copy()
set_max(temp_set)
#using a copy to keep sandbox set from being destroyed in the set_max function

#let's create a random assignment of numbers for each person in our group!
group = ['Jim', 'Jimbo', 'Jerald', 'Jimothy', 'Prince FitzJilliam III', 'Bob']
numbers = []
for i in range(len(group)):
    numbers.append(i)
#creates a list of integers for each element of the group
assignment_dict = zip(numbers, group)
#mergest the two lists, building a dictionary that almost works like a list, with numbers we can index
print(dict(assignment_dict))

#now lets use sets do something similar, but with a different goal. This time we will have more people than we have numbers.
#this process will make sure that no assignment is given to multiple members of the group.
group = {'Jill','Jeraldine','Jessica','Jamaica','Jalapenio','Jean','Billie Jean', 'Jack Johnson'}
numbers = []
for i in range(len(group)):
    numbers.append(random.randrange(15))
numbers = set(numbers)
assignment_set = zip(numbers,group)
print(set(assignment_set))