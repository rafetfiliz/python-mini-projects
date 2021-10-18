#import colorgram
#rgb_colors = []
#colors = colorgram.extract('image2.png', 30)
#for color in colors:
#    r = color.rgb.r
#    b = color.rgb.b
#    g = color.rgb.g
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#print(rgb_colors)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165),
              (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setpos(-200, 200)
n = 200
for x in range(1, 101):
    if x % 10 == 1 and x != 1:
        n -= 50
        tim.penup()
        tim.setpos(-200, n)
    color = random.choice(color_list)
    tim.dot(20, color)
    tim.penup()
    tim.forward(50)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()