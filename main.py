import turtle
import pandas

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
correct_guesses = []
score = 0

while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States guessed correctly", prompt="Guess a state").title()

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        score += 1
        state = state_data[state_data.state == answer_state]
        x = int(int(state.x.iloc[0]))
        y = int(state.y.iloc[0])
        pen.goto(x, y)
        pen.write(answer_state)



screen.exitonclick()
