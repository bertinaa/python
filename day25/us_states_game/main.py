from turtle import Screen, Turtle
import pandas

FONT=("calibre", 8, "italic")
screen = Screen()
screen.title("US Map")
image = "blank_states_img.gif"
screen.addshape(image)  # creates a screen same size as the image

t = Turtle()
t.shape(image)  # creates a turtle which is basically the map on the screen

# def get_mouse_click_coor(x,y):
#     #when we click on the state in the map, we will get the x,y coordinates
#     print(x,y)
# but we already have the coordinates in the 50_states.csv so we can just use that

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State.",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        output = pandas.DataFrame(states_to_learn)
        output.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
      #and condition bc we don't want it to keep going on when we keep guessing the same thing over and over
        t = Turtle()
        t.pu()
        t.hideturtle()
        row = data[data.state == answer_state]  # gets the row in 50_states.csv which has the answer_state
        # t.goto(row.x,row.y) cannot do this cause everything in 50_states is stored as a string
        t.goto(int(row["x"]), int(row["y"]))
        # t.write(row.state) this will also write that row.state is an object so why not just write what the user typed on the screen
        # you can avoid that by typing row.state.item(), item() just grabs the first part of the object~
        t.write(answer_state,font=FONT)
        guessed_states.append(answer_state)


#turtle.mainloop()  # will keep the screen on
# screen.exitonclick() we don't want the map to disappear when we click the screen

