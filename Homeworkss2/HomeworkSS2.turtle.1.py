from turtle import *
color("red")
speed(-1)

side = 50 # length side of the rhombus
x = 20 # smaller angle of the rhombus
n = 9 # the number of rhombuses

right(x/2)

for i in range(n):

    forward(side)
    left(x)
    forward(side)
    left(180-x)
    forward(side)
    left(x)
    forward(side)
    if i < n-1:
        right(x + 180 - 360/n)
