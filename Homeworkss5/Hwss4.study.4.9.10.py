import turtle

def draw_star(t, sz):
    """draw a 5-pointed star with size sz"""
    for i in range(5):
        t.fd(sz)
        t.right(144)

wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("pink")
for i in range(5):
    draw_star(tess, 100)
    tess.penup()
    tess.fd(350)
    tess.right(144)
    tess.pendown()
        
