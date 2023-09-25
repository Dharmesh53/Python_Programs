from bet import Turtle,Screen

t = Turtle()
screen = Screen()
t.setheading(90)
t.pensize(3)
screen.setup(width=500,height=400)


def move_fd():
    t.forward(30)


def move_bk():
    t.backward(30)


def move_lf():
    t.setheading(t.heading() + 30)
    t.forward(30)


def move_rg():
    t.setheading(t.heading() - 30)
    t.forward(30)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    t.setheading(90)


screen.listen()
screen.onkey(move_fd, "w")
screen.onkey(move_lf, "a")
screen.onkey(move_bk, "s")
screen.onkey(move_rg, "d")
screen.onkey(clear, "space")

screen.exitonclick()