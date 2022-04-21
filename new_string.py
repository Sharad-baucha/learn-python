str1 = "helloing"
str2 = "ing"
str3 = "ly"

leng = len(str1)
if len(str1) < 3:
    print(str1)

elif str1[-3:] == "ing":
    str1 = str1 + str3
    print(str1)

else:
    str1 = str1 + str2
    print(str1)
