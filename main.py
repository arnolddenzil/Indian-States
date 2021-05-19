import turtle
import pandas

screen = turtle.Screen()
screen.setup(550, 700)
screen.bgpic("Indian map.gif")
screen.title("Indian States")
correct_guesses = 0
correctly_guessed_states = []

df = pandas.read_csv("states_data.csv")
state_list = df.state.tolist()

while correct_guesses < 29:
    answer = screen.textinput(title=f"{correct_guesses}/29 States Correct", prompt="Enter the name of a state: ").title()
    if answer in state_list:
        if answer not in correctly_guessed_states:
            correctly_guessed_states.append(answer)
            correct_guesses += 1
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        x = int(df[df.state == answer].x)
        y = int(df[df.state == answer].y)
        state_turtle.goto(x, y)
        state_turtle.write(answer)


screen.exitonclick()
