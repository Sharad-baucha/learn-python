x = "My name is Sharad Shrestha"

y = str(input("Enter a letter to see whether it is repeated:"))

count = 0

for c in x:
    if c == y or c == y.upper():
        count += 1

print(y, "is repeated" ,count ,"times")