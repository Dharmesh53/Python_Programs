import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Names")
screen.screensize(canvwidth=725, canvheight=491);
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=725, height=491)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

for i in range(50):
    answer = screen.textinput(title="Guess the state", prompt="What's the another name ?").lower()
    for state in states:
        if state.lower() == answer:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            x = data[data.state == state].x
            y = data[data.state == state].y
            t.goto(int(x), int(y))
            t.write(answer)

turtle.mainloop()
