from turtle import color
from turtle import begin_fill
from turtle import forward
from turtle import left
from turtle import end_fill
#import critical turtle module sections
sides = int(input("How many sides would you like your Polygon to have? "))
user_color = input("What color would you like your Polygon to be? ")
angle = 180-((180*(sides-2))/sides)
#calculate angle to complete the shape given the number of sides.
color(user_color)
begin_fill()
#launch fill program and define color as user input
for i in range(0, sides, 1):
    forward(40)
    left(angle)
    sides += 1
#move forward, turn some amount left, and repeat for each side.
end_fill()
input("Drawing complete. Press 'Enter' to continue.")
#hold drawing open until user ends session.