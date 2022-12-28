from turtle import Turtle, Screen
from random import randint


turtle_color = ["red", "orange", "gold", "green", "blue"]
turtle_list = []
y_position = [-60, -30, 0, 30, 60]

screen = Screen()
screen.setup(width=500, height=400)


is_race_on = False

user_bet = screen.textinput(title="Make your bet!", prompt="Who will win the race?")

if user_bet:
    is_race_on = True

for turtle_index in range(0, 5):
    my_racer = Turtle(shape="turtle")
    my_racer.color(turtle_color[turtle_index])
    my_racer.penup()
    my_racer.goto(x=-240, y=y_position[turtle_index])
    turtle_list.append(my_racer)

while is_race_on:

    for turtle in turtle_list:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! Congratulations! The winner was {winning_color} turtle!")

            else:
                print(f"You've lost! The winner was {winning_color} turtle!")


screen.exitonclick()
