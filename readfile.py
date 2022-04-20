f = open("demofile.txt", "r")
print(f.read())
print("\n")
f = open("demofile.txt", "a")
f.write("\n Sharad noob mula!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())