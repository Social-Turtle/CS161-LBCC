def user_string():
    while True:
        try:
            a = str(input("Input a string! ")).lower()
        except ValueError:
            print("A string please!")
            continue
        else:
            return(a)
#function for user string input, validates evilness of input

def user_int():
    while True:
        try:
            a = int(input("Input an integer! "))
        except ValueError:
            print("An integer please!")
            continue
        else:
            return(a)
#function for user integer input, validates evilness of input

class rider:
    def __init__(self, name = 'Pat', weight = 150):
        self.name = name
        self.weight = weight
    def name(self):
        return self.name
    def weight(self):
        return self.weight
    def print_person(self):
        print(f"{self.name} weighs approximately {self.weight} pounds.")
    def __str__(self):
        return str(self.name) + ' weighs ' + str(self.weight) + ' pounds.'

#class do define the name and weight of our riders

class vehicle:
    def __init__(self, mode = 'drives', pounds = 8000, color = 'white', speed = 100, capacity = 10, sound = 'Vroom', onboard = 0):
        self.mode = mode
        self.pounds = pounds
        self.color = color
        self.speed = speed
        self.capacity = capacity
        self.sound = sound
        self.onboard = onboard
    def says(self):
        print(self.sound)
    def print_passenger(self):
        print(f'This craft is capable of carrying {self.capacity} humans safely.')
    def print_pounds(self):
        print(f'This craft is weighs {self.pounds} pounds!')
    def print_color(self):
        print(f'This craft is painted a gorgeous {self.color} color.')
    def print_speed(self):
        print(f'This craft can travel at a blazing {self.speed} miles per hour!')
    def print_mode(self):
        print(f"This craft {self.mode} to reach its destination.")
    def print_stat(self):
        print(f"With a top speed of {self.speed} miles per hour, and a passenger capacity of {self.capacity},")
        print(f"this {self.pounds} pound, {self.color} machine {self.mode} people to their destination.") 
        if self.onboard == 0:
            print("Because there are no passengers onboard, this vehicle suffers no speed reduction.")
        else:
            print(f"The vehicle is currently carrying {self.onboard} passengers onboard, roughly reducing its speed to {self.speed * (1 - (self.onboard * 136)/self.pounds)} miles per hour.")
        #this contingency statement checks whether or not to use text expressing speed reduction of the vehicle
  
    def get_on(self):
        #a user-friendly program for adding passengers to the vehicle, and reminding them how many are then aboard
        passengers = list()
        #our list for passengers later
        space = self.capacity - self.onboard
        print(f"There are {space} available seats. How many people would you like to board the vehicle?")
        added = user_int()
        self.onboard += added
        print("Please input a name, and weight in pounds for each rider.")
        if self.onboard >= self.capacity:
            #keeps user from adding more passengers than there is space
            self.onboard = self.capacity
            for i in range(space):
                new_rider = rider(user_string(),user_int())
                passengers.append(new_rider)
            print("The vehicle is now full.")
        else:
            for i in range(added):
                new_rider = rider(user_string(),user_int())
                passengers.append(new_rider)
            print(f"There are now {self.onboard} passengers aboard the vehicle.")
        return passengers
