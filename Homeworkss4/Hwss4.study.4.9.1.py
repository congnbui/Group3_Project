import turtle

def draw_square(t, sz, col, ps):
    """Make turtle draw a square of size sz and colour col with pen size ps"""	
    t.color(col)
    t.pensize(ps)
    for i in range(4):
        t.fd(sz)
        t.left(90)
    t.penup()
    t.forward(2*sz)
    t.pendown()

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.speed(-1)
for i in range(5):
    draw_square(t, 20, "pink", 4)
    

