from turtle import *
import pandas

screen = Screen()
screen.title("US States Game")
my_img = "blank_states_img.gif"
screen.addshape(my_img)
shape(my_img)

states = pandas.read_csv("50_states.csv")
states_names = states.state.tolist()
complete = True
while complete:
    answer = screen.textinput(title=f"Guess the state! States remaining: {len(states_names)}", prompt="Whats another "
                                                                                                      "state name of "
                                                                                                      "US?").title()
    if answer == "Exit":
        break
    if answer in states_names:
        x = states.x[states.state == answer]
        y = states.y[states.state == answer]
        states_names.remove(answer)
        new = Turtle()
        new.hideturtle()
        new.penup()
        new.goto(int(x), int(y))
        new.write(answer)
        #print(states_names)
    if len(states_names) == 0:
        complete = False

df = pandas.DataFrame(states_names)
df.to_csv("sates_missed.csv")
