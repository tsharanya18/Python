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

done()
