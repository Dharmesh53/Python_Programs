from turtle import Turtle, Screen
import random

turtles = []
dist = [0, 0, 0, 0, 0]
screen = Screen()
screen.setup(width=500, height=400)
colors = ["green", "red", "gold", "purple", "blue"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color :")

for i in range(0, 5):
    t = Turtle(shape="turtle")
    turtles.append(t)
    t.speed("fast")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100 + i * 40)

again = True

while again:
    idx = 0
    for turtle in turtles:
        step = random.randint(1, 20)
        turtle.forward(step)
        dist[idx] = dist[idx] + step
        idx = idx + 1
    idx = 0
    for i in dist:
        if i > 450:
            again = False
            print(dist)
            if turtles[idx].color()[0] == user_bet:
                print("You Win")
            else:
                print("You Lose")
        idx = idx + 1

screen.exitonclick()
