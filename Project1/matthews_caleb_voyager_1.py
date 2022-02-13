#A program to calculate Voyager 1's distance from the sun (resolution of 1 day)

#import datetime library for use of live distance calculation
import datetime
from datetime import date

#define today's date for program and user
todays_date = datetime.date.today()
print("_____________________________________________________________________________________________________________________________________________________________________________")
print("\nToday's date is: ", todays_date, "\n")

#initial day
launch_date = date(2009, 9,25)


choice = input("If you would like to use todays date, type 'Y'. If you would like to input your own number of days after the report, type 'N'. ")
if choice == 'Y':
    #days difference
    total_days = todays_date - launch_date
    print("\nIt has been ", total_days.days, "days since the 2009 NASA Voyager Report!")
    total_day_integer = total_days.days

if choice == 'N':
    total_day_integer = int(input("Please choose how many days after the report you would like to measure. "))

#distance equals rate (miles/day) * days total plus initial position
miles_from_sun = total_day_integer * 9177 + 16637000
kilos_from_sun = miles_from_sun * 1.609344
au_from_sun = miles_from_sun/92955887.6
#coefficient of 2 to account for round trip, and 1000 to convert kilometers to meters
radio_time = 2000*kilos_from_sun/299792458

print("\nTravelling at a blistering 38,241 mph, the Voyager 1 rocket is approximately", miles_from_sun/10000000, "x 10^10 miles from the sun. \nThat is equivalent to", kilos_from_sun/10000000 , "x 10^10 kilometers or", au_from_sun * 10 , "x 10^2 astronomical units!\n")
print("At this distance, the round trip time for radio communication to the probe is", radio_time/100, "x 10^5 seconds, or" , radio_time/360 , "x 10^2 hours!\n")
print("_____________________________________________________________________________________________________________________________________________________________________________\n")