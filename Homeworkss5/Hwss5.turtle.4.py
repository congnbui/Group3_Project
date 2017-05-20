from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    for _ in range(5):
        fd(length)
        right(144)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

# random.randint(a,b) will return a random integer N such that a <= N <= b. 
