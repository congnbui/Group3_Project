import turtle

def draw_square(t, n, sz):
    """Draw n squares that together form a flower-shaped pattern"""	
    for i in range(n):
        for j in range(4):
            t.fd(sz)
            t.left(90)
        t.right(360/n)
    
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(-1)
tess.color("blue")
tess.pensize(2)

draw_square(tess, 20, 50)
