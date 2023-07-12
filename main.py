from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
y_pos = -120
for c in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(c)
    new_turtle.goto(-240, y_pos)
    y_pos += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                is_race_on = False
            random_distance = random.randint(0, 15)
            turtle.forward(random_distance)


screen.exitonclick()
