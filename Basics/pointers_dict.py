dict1 = {
    "key1": 11
}

dict2 = dict1

print("Value of dict1 is :", dict1)
print("Value of dict2 is :", dict2)

print("dict1 points to address :", id(dict1))
print("dict2 points to address :", id(dict2))

print("\nChanging value of dict2")

dict2["key1"] = 12

print("Value of dict1 is :", dict1)
print("Value of dict2 is :", dict2)

print("dict1 points to address :", id(dict1))
print("dict2 points to address :", id(dict2))


print("\nAssigning another value of dict2")

dict2 = {
    "key1": 22
}

print("Value of dict1 is :", dict1)
print("Value of dict2 is :", dict2)

print("dict1 points to address :", id(dict1))
print("dict2 points to address :", id(dict2))
