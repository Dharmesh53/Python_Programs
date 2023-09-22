from turtle import Turtle, Screen
import heroes

print(heroes.gen())

t = Turtle()
t.shape("classic")
t.pensize(2)


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.left(angle)

# for i in range(3,11):
#     draw_shape(i)


t.speed("fastest")

for i in range(60):
    t.forward(10 + i * 5)
    t.penup()
    t.forward(10)
    t.pendown()
    t.left(80)
    t.forward(100 + i * 9)
    t.left(90)

screen = Screen()
screen.exitonclick()
