import colorgram, random
import turtle as bro
colors = colorgram.extract('image.jpg',20)
rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

t = bro.Turtle()
bro.speed("fastest")
bro.colormode(255)
t.penup()
bro.bgcolor("black")


t.setheading(210)
t.forward(520)
t.setheading(0)

for i in range(1, 500):
    t.dot(20, random.choice(rgb))
    t.forward(30)

    if i % 30 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(900)
        t.setheading(0)


screen = bro.Screen()
screen.exitonclick()