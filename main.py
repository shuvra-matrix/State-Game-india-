import turtle
from turtle import Screen, Turtle
from score import Score
import pandas as pd

screen = Screen()
score = Score()
screen.title("States Of India")
image = "india.gif"
screen.setup(width=620, height=745)
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("india.csv")
data_list = data.state.to_list()

States = []
remaining_state = []
while len(States) < 39:
    user_input = screen.textinput(title="Enter Details",
                                  prompt="Enter States Name And\nUnion Territory Name Or\nType Exit to Quit").title()
    if user_input == "Exit":
        for state_details in data_list:
            if state_details not in States:
                remaining_state.append(state_details)

        pd.DataFrame(remaining_state).to_csv("remaining_state.csv")
        break
    if user_input in data_list:
        if user_input not in States:
            States.append(user_input)
            tim = Turtle()
            tim.penup()
            tim.shapesize(0.1)
            tim.shape("circle")
            state_data = data[data['state'] == user_input]
            tim.goto(int(state_data.x), int(state_data.y))
            tim.write(f"{user_input}",font=("Arial", 10, "normal"))
            score.update_score()
