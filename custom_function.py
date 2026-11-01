from numbers import result


def greet():
    print("Hello")

# greet()

def greeting(name):
    print(f"Hello {name}")

def volume_cylinder(radius,height):
    v=22/7*radius**2*height
    print(v)

# volume_cylinder(5,8)

def volume_cylinder_2(radius,height):
    v = 22 / 7 * radius ** 2 * height
    return v

def volume_surface(radius,height):
    v = 22 / 7 * radius ** 2 * height
    a=22 / 7 * radius ** 2 * 2 + 22/7 * radius*2 *height

    return v,a

def divide(a,b, should_round):
    res= a/b
    if should_round==True:
        return round(res,2)
    else:
        return res

print(divide(9,5.11,True))

# volume,area=volume_surface(10,20)
# print(f"Volume is {volume} and Area is {area}")


# result = volume_cylinder_2(6.5,8.9)
# print(round(result,3))
# greeting('Sila')
# greeting('Samia')