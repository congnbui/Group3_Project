def area_of_circle(r):
    """area of a circle with radius r"""
    import math
    a = math.pi * (r**2)
    return a

##import math

while True:
    r = int(input("Enter the radius: "))
    print("The area of the circle is: ",area_of_circle(r))
