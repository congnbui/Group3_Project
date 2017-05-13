from turtle import *

colors = ["red", "blue", "brown", "yellow", "grey", "purple"]
length = 100
width = 65

for i, j in enumerate(colors):
    color(j, j)
    begin_fill()
    right(90)
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    if i < len(colors) -1:
        forward(2* width)
    else:
        forward(width)
    end_fill()


    
