import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = 'blank_states_img.gif'
screen.setup(800,600)
screen.addshape(image)
turtle.shape(image)



# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
data = pandas.read_csv('50_states.csv')
state_list = data["state"].to_list()
state_count = len(state_list)
player_count = 0
guessed_states =[]

while player_count < state_count:
    answer_state = screen.textinput(title=f"Score : {player_count}/{state_count}", prompt="What's the State's name? ").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)
        player_count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(answer_state)


# missed_states = []
# for state in state_list:
#     if state not in guessed_states:
#         missed_states.append(state)
missed_states=[state for state in state_list if state not in guessed_states]

print(missed_states)

missing_data = pandas.DataFrame(missed_states)
missing_data.to_csv("States_to_learn.csv")
