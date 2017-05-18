import turtle

def draw_poly(t, n, sz):
    """Make turtle draw a n-sided regular polygon with size sz"""	
    for i in range(n):
        t.fd(sz)
        t.left(360/n)

def draw_equitriangle(t, sz):
    """Draw equilateral triangle"""
    draw_poly(t, 3, sz)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(-1)
tess.color("pink")
tess.pensize(4)

draw_equitriangle(tess, 50)
