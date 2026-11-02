#Functions/Methods
with open("temp.txt", "w") as file:
    file.write("99.36\n")
    file.write("156\n")
    file.write("54.34\n")
with open("temp.txt", "r") as file:
    content=file.read()
    print(content)