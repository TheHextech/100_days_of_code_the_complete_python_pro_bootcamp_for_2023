from turtle import Turtle, Screen
import random

new_turtle = Turtle()
screen = Screen()
new_turtle.speed(10)

screen.setup(width=500, height=400)
is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color: {colors}")

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(10)
    new_turtle.goto(x=-200, y=-150 + (50 * turtle_index))
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Your turtle won!!!! The {winning_color} turtle is the winner!")
            else:
                print(f"The {winning_color} turtle won. Not yours!")
        else:
            turtle_sprint = random.randint(0, 10)
            turtle.forward(turtle_sprint)

screen.exitonclick()