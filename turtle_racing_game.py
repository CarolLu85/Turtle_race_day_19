
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "green", "pink", "blue", "orange", "yellow"]
my_turtles = []
y = -70
for turtles_number in range(0,6):
    turtle_object = Turtle("turtle")
    turtle_object.color(color[turtles_number])
    my_turtles.append(turtle_object)
    turtle_object.penup()
    turtle_object.goto(-240,y)
    y += 30


player_choice = screen.textinput("Make your bet", "please enter a color of the turtle:  ")
game_on = True
while game_on:
    for turtle in my_turtles:
        turtle.forward(random.randint(1,10))
        if turtle.xcor() > 240:
            game_on = False
            if player_choice == turtle:
                print(f"You win. The winner is {turtle.pencolor()}!")
            else:
                print(f"You lose. The winner is {turtle.pencolor()}")

screen.exitonclick()