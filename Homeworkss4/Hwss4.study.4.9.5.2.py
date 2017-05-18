import turtle
import math

def draw_square(t, n, sz):
    """Draw n quasi-squares that together form a weird pattern"""	
    x = sz
    for i in range(n):
        for j in range(4):
            t.right(89)
            t.fd(sz)
            sz = sz + x

       
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(-1)
tess.color("blue")
tess.pensize(1)

draw_square(tess, 24, 2)
