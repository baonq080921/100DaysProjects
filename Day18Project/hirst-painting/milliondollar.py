# import colorgram
# # rgb_colors = []
# # colors = colorgram.extract('image.jpg', 30)
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.g
# #     b = color.rgb.b
# #     new_color = (r, g, b)
# #     rgb_colors.append(new_color)
# # print(rgb_color)
import turtle as turtle_module
import random
timmy = turtle_module.Turtle()
turtle_module.colormode(255)
timmy.shape("arrow")
timmy.pu()
timmy.speed("fastest")
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
color_list = [(231, 234, 240), (235, 232, 225), (239, 230, 236), (226, 236, 231), (202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106,
                                                                                                                                                                                                                                      193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]
dot=100
for dot_count in range(1,dot+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
