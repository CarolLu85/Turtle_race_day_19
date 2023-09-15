
from turtle import Turtle, Screen
import random

color = ["red", "green", "pink", "blue", "orange", "yellow"]
turtles = Turtle()
turtles = []
# turtles.penup()
# turtles.shape("turtle")

class MyTurtles:

    def __init__(self, name, color):
        self.shape = "turtle"
        self.openup()
        self.color = color
        self.name = name


class RaceTurtles:
    def my_turtles(self):
        self.turtles = [
        MyTurtles("1", color[0]), MyTurtles("2", color[1]),
        MyTurtles("3", color[2]), MyTurtles("4", color[3]),
        MyTurtles("5", color[4]),MyTurtles("6", color[5])
        ]

    def get_names(self):
        for a in range(5):
            turtles[a].append(self.turtles[a])


a = -150
for name in turtles:
    name.goto(-245, a)
    a += 30


for name in turtles:
    name.speed(random.randint(1,10))






screen = Screen()
screen.setup(width=500, height=400)
screen.textinput("Make your bet", "please enter a color of the turtle:  ")

yiyi.speed(random.randint(1,10))
mama.speed(random.randint(1,10))
baba.speed(random.randint(1,10))

yiyi.goto(-245, 0)
mama.goto(-245, 20)
baba.goto(-245, -20)
screen.exitonclick()