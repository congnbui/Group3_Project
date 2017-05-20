from turtle import *

def draw_square(length, colour):
    color(colour)
    for _ in range(4):
        fd(length)
        right(90)

draw_square(100,"green")



