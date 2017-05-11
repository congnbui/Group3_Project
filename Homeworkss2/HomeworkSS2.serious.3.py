print("Print stars and xs")

n = 40 # the number of stars

print("*" * n)

print("x*" * n)

print()

x = 10 # the number of rows
y = 10 # the number of columns

for i in range(x):
    if i % 2 ==0:
        print("x*" * y)
    else:
        print("*x" * y)
    
