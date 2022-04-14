#a = []
#b = list()
#print(type(a))
#print(type(b))
# a.sort

a = []
for i in range(1 , 31):
    if i % 5 == 0:
        a.append(i)
print(a)

b = [69 , 69 , 69]
a.extend(b)

print(a)
print(a[2:5])

print(a[::-1])

c = [10 , 20 , 30 , 10 , 10 ,66]
c.remove(10)
print(c)