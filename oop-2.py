class Circle:
    def __init__(self,r):#set up
        self.radius = r
    def area(self):
        return  22/7 * self.radius**2
    def perimeter(self):
        return  22/7 * self.radius*2
    def print_details(self):
        print("Radius is", self.radius)
        print("Area is", self.area())
        print("Perimeter is", self.perimeter())

c1=Circle(7)
c2=Circle(14)
c3=Circle(15)

print(c1.area())
