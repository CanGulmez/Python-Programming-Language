# JSON MODULE

import json

person_string = '{"name": "Can", "languages": ["python", "kotlin"]}'   # JSON string

# JSON string to dict:

result = json.loads(person_string)

# print(result)
# print(type(result))

print("-----------------------------")

# with open("person.json") as file:
#     result = json.load(file)
#     print(result)

print("----------------------")

# Dict to JSON string:

person_dict = {
    "name": "Can",
    "languages": ["Python", "C#"]
}

result = json.dumps(person_dict)
print(result)
print(type(result))

print("----------------------------")

file = open("person.json", "w")
result = json.dump(person_dict, file)
print(result)
# file.close()