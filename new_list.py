# thislist = [15 , 88 , 45 , 47 , 420 , 599]

# for i in thislist:
#     print(i)

# keys = ['A','B','C']
# values = [65,66,67]

# thisdict = {}

# for i in range(0 , len(keys)):
#     thisdict[keys[i]] = values[i]
    
# #print(thisdict.items())
# print(thisdict)

# firstname = "sharad"
# lastname = "shrestha"
# value = {"firstname":"sharad","lastname":"shrestha"}
# student = {"name":value}

# print(student["name"]["lastname"])

student = {
    "name" : {"firstname":"sharad" , "lastname":"shrestha"},
    "rollno" : 69,
    "class" : "CSIT"
}

print(student["name"]["firstname"])