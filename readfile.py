# f = open("demofile.txt", "r")
# print(f.read())
# print("\n")
# f = open("demofile.txt", "a")
# f.write("\n Sharad noob mula!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile.txt", "r")
# print(f.read())

# str1 = "hello world"
# print(str1.replace("hello","noob"))

f = open("demofile.txt", "r")
str1 = f.read()
print(str1)

data = str1.replace("noob", "good")

g = open("output.txt", "w")
g.write(data)

f.close()
g.close()