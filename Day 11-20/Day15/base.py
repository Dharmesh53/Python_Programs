from turtle import Turtle,Screen

timmy = Turtle()
myScreen = Screen()
timmy.shape("turtle")
timmy.color("coral")
while True:
    timmy.forward(100)
    timmy.backward(100)
print(timmy)
print(myScreen.canvheight)
myScreen.exitonclick()