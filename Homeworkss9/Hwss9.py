class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_xy(self):
        print("({0}, {1})".format(self.x, self.y))
    def distant(self, otherpoint):
        return ((self.x - otherpoint.x)**2 + (self.y - otherpoint.y)**2)**0.5
    def halfway(self, otherpoint):
        return Point((self.x + otherpoint.x)/2, (self.y +otherpoint.y)/2)
    def reflex_x(self):
        return Point(self.x, -self.y)
    def reflex_y(self):
        return Point(-self.x, self.y)
    def reflex_origin(self):
        return Point(-self.x, -self.y)
    def get_line_to(self, otherpoint):
        ### y = a * x + b###
        if self.x == otherpoint.x and self.y == otherpoint.y:
            return None
        if self.x == otherpoint.x:
            return "x = " + str(self.x)
        elif self.y == otherpoint.y:
            return "y = " + str(self.y)
        else:
            a = (self.y - otherpoint.y)/(self.x - otherpoint.x)
            b = self.y - a * self.x
            if b > 0:
                return "y = " + str(a) + "*x + " + str(b)
            elif b == 0:
                return "y = " + str(a) + "*x"
            else:
                return "y = " + str(a) + "*x - " + str(-b)


class Rectangle():
    def __init__(self, p, w, h):
        self.position = p
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return  (self.width + self.height) * 2
    def flip(self):
        return Rectangle(self.position, self.height, self.width)
    def contain(self, point):
        if self.position.x <= point.x <= (self.position.x + self.width) and (self.position.y - self.height) <= point.y <= self.position.y:
            return True
        return False


point_a = Point(2, 1)
point_b = Point(10,9)
print(point_a.distant(point_b))
point_a.halfway(point_b).print_xy()
point_a.reflex_x().print_xy()
point_a.reflex_y().print_xy()
point_a.reflex_origin().print_xy()
print(point_a.get_line_to(point_b))

reg_1 = Rectangle(point_a, 10, 5)
print(reg_1.area())
print(reg_1.perimeter())
reg_1_flip = reg_1.flip()
point_c = Point(8, -2)
print(reg_1.contain(point_c))
print(reg_1_flip.contain(point_c))