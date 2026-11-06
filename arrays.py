#store many values

ages =[21,72,43,16,23,13,36,54,5,32] #list

names=["Jack","John","Anny","Benson"]

#functions
ages.append(31)

print(ages)

ages.sort()
print(ages)
ages.reverse()
print(ages)

names.sort()
print(names)

jack=names.count("Jack")
print(jack)

print(len(ages))
print(len(names))

print(sum(ages))
print(sum(ages)/len(ages))

print(names[0])
print(names[-1])

print(names[-3:])
print(names[1:3])

#sets

scores={88,78,88,65,77,78}
print(scores)

#tuples

weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday")

print(weekdays[0])

#dictionary

person={"name":"Jason","age":22,"weight":53,"height":1.88}

print(person["name"])
print(person["age"])

people=[
    {"name":"Aria","age":29},
    {"name":"Joseph","age":49},
    {"name":"Gabriel","age":19}
]
print(people[0]["age"])
print(people[0])















