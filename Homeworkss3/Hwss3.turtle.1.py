from turtle import *
speed(-1)
colors = ["red", "blue", "brown", "yellow", "grey", "cyan", "purple"]

##for i in range(3, len(colors)+3):
##    color(colors[i-3])
##    for j in range(i):
##        forward(100)
##        left(360/i)
        
##for i, j in enumerate(colors):
##    color(j)
##    for k in range(i+3):
##        forward(100)
##        left(360/(i+3))


# make the codes work without fail
number_of_shapes = 17

color_index = 0

for i in range(number_of_shapes, 2, -1):
    color(colors[color_index % len(colors)])
    color_index +=1
    for j in range(i):
        forward(20)
        left(360/i)
