import turtle as t
from turtle import Screen
from random import random, choice


def get_color():
    r = random()
    g = random()
    b = random()
    return [r, g, b]


direction = [270, 90, 180, 0]

tim = t.Turtle()
tim.width(6)
tim.speed("fastest")

for _ in range(300):
    c = get_color()
    tim.pencolor(c[0], c[1], c[2])
    tim.forward(30)
    tim.seth(choice(direction))

screen = Screen()
screen.exitonclick()
