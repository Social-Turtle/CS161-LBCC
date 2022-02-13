import calebtools
import test_vehicle


print("\n\nHello, user! Welcome to the vehicle construction program.")
print("Today, we shall walk you through a simple process to help you dream up your new favorite vehicle!")

print('\n\nFirst, how does your vehicle move? Fill in the blank: My vehicle _________ to its destination.')
blueprint = []
#generating list to add user items to, we use this to generate their vehicle at the end in one step
blueprint.append(calebtools.user_string())

print("\n\nNext, how much (in pounds) does your vehicle weigh?")
blueprint.append(calebtools.user_int())

print("\n\nWhat color is your vehicle? Fill in the blank: My vehicle is colored _______.")
blueprint.append(calebtools.user_string())

print("\n\nWhat is your vehicle\'s top speed in Miles per Hour?")
blueprint.append(calebtools.user_int())

print("\n\nHow many passengers can your vehicle carry?")
blueprint.append(calebtools.user_int())

print("\n\nFinally, what does your vehicle sound like?")
blueprint.append(calebtools.user_string())

print("\n\nAlright, now let's take a look at what you've created!")
user_vehicle = calebtools.vehicle(*tuple(blueprint))
#compiling our inputs into a tuple, which can then be input as a roadmap for our object to be created.
user_vehicle.print_stat()

print("\n\nNow we will experiment with adding and removing passengers from our craft!")
people = user_vehicle.get_on()
user_vehicle.print_stat()
#performs process of adding passenger objects to the vehicle (stored as a list called 'people')

for i in range(len(people)):
    print(people[i])
#restating our inputs for the user

people_weight = 0
for i in range(len(people)):
    people_weight += people[i].weight
#summarizing total passenger weight.

print("\n\nThanks for designing your dream vehicle with us, we hope to see you again soon!")
input("Press any key to exit.")