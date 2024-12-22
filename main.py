import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
correct_guessess = []

while len(correct_guessess) != 50:
    answer_state = screen.textinput(title=f"{len(correct_guessess)}/50 States Correct", prompt="What's another state's name?").capitalize()
    if answer_state in states:
        correct_guessess.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.speed(10)
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x=int(data[data.state == answer_state].x), y=int(data[data.state == answer_state].y))
        new_turtle.write(answer_state, font=('Arial', 10, 'bold'))

screen.exitonclick()
