import turtle

def draw_square(t, sz, col, ps, step):
    """Make turtle draw a square of size sz and colour col with pen size ps"""	
    t.color(col)
    t.pensize(ps)
    for i in range(4):
        t.fd(sz)
        t.left(90)
    t.penup()
    t.goto(t.pos()+ (-step,-step))
    t.pendown()
    

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.speed(-1)
sz = 20
col = "pink"
ps = 4
step = 10
for i in range(5):
    draw_square(t, sz, col, ps, step)
    sz += 2*step
    
    


