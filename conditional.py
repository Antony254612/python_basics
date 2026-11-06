name=input("What is your name?:")

age=input("Enter your age:")

if not age.isnumeric():
    print("Invalid age")
#     terminate



if int(age)>18:
    print( name +" is an Adult")
else:
    print(name +" is a Child")