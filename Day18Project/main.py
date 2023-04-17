
from turtle import Turtle, Screen
import turtle as t
import random
t_turtle = Turtle()
t_turtle.shape("blank")
# colors = ["#4169E1", "#A0522D", "#FF0000", "#FFE4E1", "#8A2BE2"]

# def draw_shape(numb_size):
#     angle=360/numb_size
#     for i in range(numb_size):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for i in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(i)

# My way:
# n=3
# while n <11:
#     for i in range(n):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(360/n)
#     timmy_the_turtle.color(random.choice(colors))
#     n+=1

a = [0, 90, 180, 270]
t.colormode(255)
def random_color():
    random_red=random.randint(0,255)
    random_green=random.randint(0,255)
    random_blue=random.randint(0,255)
    random_color=(random_red,random_green,random_blue)
    return random_color
def move(angle_r):
    t_turtle.speed(0)
    t_turtle.pensize(10)
    t_turtle.forward(20)
    t_turtle.setheading(angle_r)
    t_turtle.forward(20)

n=200
for i in range(n):
    t_turtle.color(random_color())
    move(random.choice(a))


screen = Screen()
screen.exitonclick()
