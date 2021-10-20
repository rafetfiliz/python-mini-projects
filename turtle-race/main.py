from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_list = []
colors = ["red", "violet", "green", "blue", "indigo", "yellow", "orange"]
y = 210
is_race_on = False

for i in range(7):
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.turtlesize(2, 2, 2)
    my_turtle.goto(-350, y)
    y -= 70
    turtle_list.append(my_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(7):
        random_distance = random.randint(0, 10)
        turtle_list[i].forward(random_distance)
        turtle_coordinate = turtle_list[i].xcor()
        if turtle_coordinate >= 350:
            is_race_on = False
            if user_bet == colors[i]:
                result = f"Congratulations, you guessed correct! {colors[i].capitalize()} turtle won the race."
                print(result)
            else:
                result = f"You guessed wrong! {colors[i].capitalize()} turtle won the race."
                print(result)


screen.exitonclick()
