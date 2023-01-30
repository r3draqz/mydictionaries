person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

# name of second child
print(type(person["children"]))
print(person["children"][1])


# name of cat
print(type(person["pets"]["cat"]))
print(person["pets"]["cat"])


# use for loop to list each child
for child in person["children"]:
    print(child)

# print out the pets in this format;
# 'type of pet: dog name of pet: Fido'
for pet, name in person["pets"].items():
    print(f"Type of pet: {pet} name of pet: {name}")
