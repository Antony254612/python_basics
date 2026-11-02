def add(a,b,c):
    res=a+b+c
    return res

def addition(*nums):
    total = sum(nums)
    return total

def build_profile(**kwargs):
    for k,w in kwargs.items():
        print(f"{k} :{w}")

def fancy_function(name,*nums,**kwargs):
    print(name)
    print(nums)
    print(kwargs)

# def square(num):
#     return  num*num
# res=square(4)

square = lambda num:num *num

surface_area_cylinder=lambda r,h :22/7*r**2 *2 +22/7*2*r*h

# print(surface_area_cylinder(7,20))
people=[
    {"name":"Alex","age":46},
    {"name":"Alice","age":62},
    {"name":"Alan","age":26},
    {"name":"Phanice","age":29},
    {"name":"Alex","age":36},
]
sorted_by_age= sorted(people,key=lambda x:x["age"],reverse=True)

"""
returns the sum of all numbers passed as arguments
parameters integers
"""
print(sorted_by_age)

# print(square(5))

# #call function
# print(add(9,7,5))
# print(addition(4,6,5,5))
# print(addition(2,8,4,3,10))
# build_profile(experience=100,name="Jane",age="19",profession="Software Engineer")
