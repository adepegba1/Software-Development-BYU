# Write a program to find the youngest person in the list.
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
young_age = 999999999999
young_name = "David"
for person in people:
    person = person.split(" ")
    name = person[0]
    age = int(person[1])
    if young_age > age:
        young_age = age
        young_name = name
print(f"The youngest person is {young_name} and the age is {young_age}")

    
    
