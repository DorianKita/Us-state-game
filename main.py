import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
x_coor = data.x
y_coor = data.y
correct_answers = 0

while correct_answers != 50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="What's another state's name?").capitalize()
    if answer_state in states:
        correct_answers += 1
        new_turtle = turtle.Turtle()
        new_turtle.speed(3)
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x=int(data[data.state == answer_state].x), y=int(data[data.state == answer_state].y))
        new_turtle.write(answer_state, font=('Arial', 10, 'bold'))

screen.exitonclick()
