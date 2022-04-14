print("LCM of two numbers:-")

a = int(input("Enter 1st number:"))

b = int(input("Enter 2nd number:"))

c = []
d = []

while a > 1:
    if a % 2 == 0:
        a = a // 2
        c.append(2)
    elif a % 3 == 0:
        a = a // 3
        c.append(3)
    else:
        c.append(a)
        a = 1

print(c)

while b > 1:
    if b % 2 == 0:
        b = b // 2
        d.append(2)
    elif b % 3 == 0:
        b = b // 3
        d.append(3)
    else:
        d.append(b)
        b = 1

print(d)     

lcm = []

for i in range(len(c)):
    i = 0
    for j in range(len(d)):
        if c[i] == d[j]:
            lcm.append(c[i])
            del c[i]
            del d[j]
            break
        elif j == len(d) - 1:
            lcm.append(c[i])
            del c[i]
    
#if len(c) != 0:
    #for i in range( 0 , len(c) , 1):
        #lcm.append(c[i])


if len(d) != 0:
    for i in range(len(d)):
        lcm.append(d[i])

print(lcm)

ans = 1

for i in range(len(lcm)):
    ans = ans * lcm[i]

print("The required LCM is", ans)