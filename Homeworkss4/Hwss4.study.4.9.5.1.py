import turtle

def draw_square(t, n, sz):
    """Draw n squares that together form a weird pattern"""	
    x = sz
    for i in range(n-1):
        for j in range(4):
            t.right(90)
            t.fd(sz)
            sz += x

    for j in range(3):
        t.right(90)
        t.fd(sz)
        sz += x
    t.right(90)
        
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(-1)
tess.color("blue")
tess.pensize(1)

draw_square(tess, 20, 3)
