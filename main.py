
# grades = {
#     "alice":85,
#     "Bob":78,
#     "Charlie":92
# }

# #add new student
# grades["david"] = 88
# del grades["Charlie"]
# print("initial grades: ", grades)

# for name, grade in grades.items():
#     print(f"Name: {name}\tGrade: {grade}")
  
# pets = {
#     "Jake":"Golden Retriver",
#     "Sam":"Desert cat",
#     "bob":"brown mouse",
# }

# for name, breed in pets.items():
#     print(f"{name} owns a {breed}")
  
# people = {
#      "Jake":["Jiggy","604-811-3862"],
#     "Sam":["Desert cat","724-388-9080"],
#     "bob":["brown mouse","188-988-2300"],
# }

# for firstname, lastname in people.items():
#     print(f"Firstname: {firstname}\t Lastname: {lastname[0]}\t Number: {lastname[1]}")

cities = {
    "Vancouver":["Canada","700,000","First known as Gastown"],
    "Sydney":["Australia","5.2 Million","One in eight people are over 65 years old in Sydney."],
    "Moscow":["Russia","13.1 Million", "Largest amount of libraries in the world"]
}

for city, info in cities.items():
    print(f"City: {city}\nCountry: {info[0]}\nPopulation: {info[1]}\nFact: {info[2]}\n")

