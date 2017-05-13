from turtle import *

colors = ["red", "blue", "brown", "yellow", "grey"]

##for i in range(3, len(colors)+3):
##    color(colors[i-3])
##    for j in range(i):
##        forward(100)
##        left(360/i)
        
for i, j in enumerate(colors):
    color(j)
    for k in range(i+3):
        forward(100)
        left(360/(i+3))
        
