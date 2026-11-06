#oop(object oriented programming)
# classes
from numbers import result


class Person:
    #constructor function
    def __init__(self,name,dob,color,weight,height):
        self.name=name
        self.dob=dob
        self.color=color
        self.weight=weight
        self.height=height
    def display(self):
        print(f"Name is {self.name} and dob is {self.dob}")

    def get_bmi(self):
        result =self.weight/self.height**2
        return round(result,2)

# A class is a blue print for creating objects

p1=Person("Lopez Ramon","08-12-1990","Black",65.56,2.34)
p2=Person("John Lucas","13-09-2006","white",46.5,1.06)

p1.display()
p2.display()
print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p1.name} bmi is {p1.get_bmi()}")