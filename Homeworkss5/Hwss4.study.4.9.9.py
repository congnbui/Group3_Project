import turtle

def draw_star(t, sz):
    """draw a 5-pointed star with size sz"""
    for i in range(5):
        t.fd(sz)
        t.right(144)
        

tess = turtle.Turtle()
tess.pensize(3)
draw_star(tess, 100)
        
