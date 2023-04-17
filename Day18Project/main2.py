from turtle import Turtle, Screen
import turtle as t
import random
t_turtle = Turtle()
t_turtle.shape("arrow")
t.colormode(255)
t_turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


def draw_spinograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        t_turtle.color(random_color())
        t_turtle.circle(100)
        t_turtle.setheading(t_turtle.heading()+size_of_gap)


draw_spinograph(5)

screen = t.Screen()
screen.exitonclick()
