import calebtools 

class vehicle:
    #defining a class
    def __init__(self, mode, wheels, color, speed, passengers, sound):
        self.mode = mode
        self.wheels = wheels
        self.color = color
        self.speed = speed
        self.passengers = passengers
        self.sound = sound
    #defining attributes of the object
    def says(self):
        print(self.sound)
    def print_passenger(self):
        print(f'This craft is capable of carrying {self.passengers} humans safely.')
    def print_wheels(self):
        print(f'This craft is equipped with {self.wheels} wheels!')
    def print_color(self):
        print(f'This craft is painted a gorgeous {self.color} color.')
    def print_speed(self):
        print(f'This craft can travel at a blazing {self.speed} miles per hour!')
    def print_mode(self):
        print(f"This craft {self.mode} to reach its destination.")
    def print_stat(self):
        print(f"With a top speed of {self.speed} miles per hour, and a passenger capacity of {self.passengers},")
        print(f"this {self.wheels} wheeled, {self.color} machine {self.mode} people to their destination.")
    #defining print functions for attribute outputs

plane = vehicle('flies', 4, 'blue', 600, 300, 'Nyyyyyoooom')
#a random, non-default class instance
plane.print_passenger()
plane.print_wheels()
plane.print_color()
plane.print_speed()
plane.print_mode()

print('\nOr, we can compile each function into one larger data-method:\n')
plane.print_stat()

print('Now we will make a new object!')
car = vehicle('drives', 4, 'red', 100, 6, 'Skrrrrch')
car.print_stat()

print('That was fun! We should do one more.')
boat = vehicle('paddles', 4, 'white', 50, 15, 'Blublublublublub')
boat.print_stat()

print('Next, we shall check if any of our parameters are the same!')
print('Checking if speed matches')
print(car.speed == boat.speed == plane.speed)
print('Checking if passenger capacity matches')
print(car.passengers == boat.passengers == plane.passengers)
print('Checking if color matches')
print(car.color == boat.color == plane.passengers)
print('Checking if mode matches')
print(car.mode == boat.mode == plane.mode)
print('Checking if number of wheels match')
print(car.wheels == boat.wheels == plane.wheels)
print('Wow, it looks like the vehicles all have the same number of wheels!')
print('This is probably because the boat is a duck boat!')
#proving uniqueness as individual instances of a class
boat.says()
car.says()
plane.says()
#my fun because I like vehicle noises