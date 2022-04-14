# a = [1,2,3,4,5,6]
# print(type(a))

# a = tuple(a)
# print(type(a))

# a = {
#     1:"a",
#     True:"True"
# }

# print(a[True])
# print(a)

# #a['name'] = 'Sharad'
# a["name"] = "Sharad"

# print(a)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x)
