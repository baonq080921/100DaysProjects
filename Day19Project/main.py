from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def tilted_clockwise():
    new_heading=timmy.heading()-10
    timmy.seth(new_heading)
def tilted_counter():
    new_heading=timmy.heading()+10
    timmy.seth(new_heading)
    
def clear_screen():
    timmy.clear()
    timmy.pu()
    timmy.home()
    timmy.pd()
def move_cirlce():
    timmy.circle(50,10)


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward, "s")
screen.onkey(tilted_clockwise, "d")
screen.onkey(tilted_counter,"a")
screen.onkey(clear_screen,"c")
screen.onkey(move_cirlce,"r")
screen.exitonclick()
