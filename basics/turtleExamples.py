from turtle import *

# square
for i in range(4):
    forward(50)
    right(90)

# star
for i in range(5):
    forward(50)
    right(144)

# hexagon
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    forward(side_length)
    right(angle)

penup()
for i in range(1, 400, 50):
    print(i)
    right(90)
    forward(i)
    right(270)
    pendown()
    circle(i)
    penup()
    home()

penup()
forward(25)
# right(90)
# forward(25)
right(270)
circle(25)

# done()
