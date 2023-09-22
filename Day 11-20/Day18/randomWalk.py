import random
from turtle import Turtle, Screen

t = Turtle()

colors = ["green", "red", "cyan", "yellow", "magenta", "gold", "orchid", "navy"]

direction = [0, 90, 180, 270]

t.pensize(15)
t.speed("fastest")

for i in range(1000):
    t.forward(20)
    t.color(random.choice(colors))
    t.setheading(random.choice(direction))
