import turtle

def draw_poly(t, n, sz):
    """Make turtle draw a n-sided regular polygon with size sz"""	
    for i in range(n):
        t.fd(sz)
        t.left(360/n)
    
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(-1)
tess.color("pink")
tess.pensize(4)

draw_poly(tess, 8, 50)
