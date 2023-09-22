import random
import turtle as bro

t = bro.Turtle()

t.speed("fastest")
bro.colormode(255)
t.pensize(3)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def spirograph(gap):
    for i in range(int(360 / gap)):
        t.color(random_color())
        t.circle(150)
        t.setheading(t.heading() + gap)


spirograph(5)

screen = bro.Screen()
screen.exitonclick()
