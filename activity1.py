# import os
# os.environ["TK_SILENCE_DEPRECATION"] = "1"
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forwatd(side_length)
    polygon.right(angle)
turtle.done()