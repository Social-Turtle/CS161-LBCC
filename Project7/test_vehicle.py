import calebtools
#mode = 'drives', pounds = 8000, color = 'white', speed = 100, capacity = 10, sound = 'Vroom', onboard = 0
stock_vehicle = calebtools.vehicle()
stock_rider = calebtools.rider()
#defines default versions of our class instances

class tests:
    #a series of tests (as simple as possible) checking that our default values are correct.
    def vehicle_mode(vehicle):
        if vehicle.mode == 'drives':
            default_mode = True
            print(f'Default mode: {default_mode}')
    def vehicle_pounds(vehicle):
        if vehicle.pounds == 8000:
            default_pounds = True
            print(f'Default pounds: {default_pounds}')
    def vehicle_color(vehicle):
        if vehicle.color == 'white':
            default_color = True
            print(f'Default color: {default_color}')
    def vehicle_speed(vehicle):
        if vehicle.speed == 100:
            default_speed = True
            print(f'Default speed: {default_speed}')
    def vehicle_capacity(vehicle):
        if vehicle.capacity == 10:
            default_capacity = True
            print(f'Default capacity: {default_capacity}')
    def vehicle_sound(vehicle):
        if vehicle.sound == 'Vroom':
            default_sound = True
            print(f'Default sound: {default_sound}')
    def vehicle_onboard(vehicle):
        if vehicle.onboard == 0:
            default_onboard = True
            print(f'Default onboard: {default_onboard}') 
    def default_gammot(vehicle):
        #assimilating individual functions into one comprehensive litmus test for the vehicle class
        tests.vehicle_mode(stock_vehicle)
        tests.vehicle_pounds(stock_vehicle)
        tests.vehicle_color(stock_vehicle)
        tests.vehicle_speed(stock_vehicle)
        tests.vehicle_capacity(stock_vehicle)
        tests.vehicle_sound(stock_vehicle)
        tests.vehicle_onboard(stock_vehicle)
    def rider_name(rider):
        if rider.name == 'Pat':
            default_name = True
            print(f'Default name: {default_name}')
    def rider_weight(rider):
        if rider.weight == 150:
            default_weight = True
            print(f'Default weight: {default_weight}')
    def rider_gammot(rider):
        tests.rider_name(rider)
        tests.rider_weight(rider)

tests.default_gammot(stock_vehicle)
tests.rider_gammot(stock_rider)
#running the two primary tests.