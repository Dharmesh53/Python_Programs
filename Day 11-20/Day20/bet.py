from turtle import Turtle, Screen
import random

turtles = []
screen = Screen()
screen.setup(width=500, height=400)
colors = ["green", "red", "gold", "purple", "blue"]

# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color :")

for i in range(0, 5):
    t = Turtle(shape="turtle")
    turtles.append(t)
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100 + i * 40)


for turtle in turtles:
    turtle.forward(random.randint(1, 20))

screen.exitonclick()