from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# def move_forward():
#     tim.forward(10)
#
# screen.onkey("space", move_forward)


def moving_forward():
    tim.forward(10)


def moving_backward():
    tim.backward(10)


def moving_counter_clockwise():
    tim.circle(-10)

def moving_colowise():
    tim.circle(10)


def screen_clearing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(moving_forward, "W")
screen.onkey(moving_backward, "B")
screen.onkey(moving_counter_clockwise, "S")
screen.onkey(moving_colowise, "D")
screen.onkey(screen_clearing, "C")

screen.exitonclick()