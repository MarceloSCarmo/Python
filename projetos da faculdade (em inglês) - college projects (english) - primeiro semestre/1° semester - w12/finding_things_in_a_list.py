

people_list = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

official_youngest_age = 100
official_youngest_person = ''

for people in people_list:
    data = people.split(" ")

    youngest_person = data[0]
    youngest_age = int(data[1])

    if official_youngest_age > youngest_age:
        official_youngest_age = youngest_age
        official_youngest_person = youngest_person

print(f"Who's the youngest person in the list?\n")
print(f'Age: {official_youngest_age} years old, name: {official_youngest_person}')