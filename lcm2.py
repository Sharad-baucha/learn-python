print("LCM of two numbers:-")

a = int(input("Enter 1st number:"))

b = int(input("Enter 2nd number:"))

c = []
d = []

def get_prime_factors(num):
    factors = []
    while num > 1:
        for i in range(2 , num + 1):
            if num % i == 0:
                factors.append(i)
                num = num // i
                break 
    return factors

c = get_prime_factors(a)
d = get_prime_factors(b)

print(c)
print(d)

"""
while a > 1:
    for i in range(2 , a + 1):
        if a % i == 0:
            c.append(i)
            a = a // i
            break

print(c)

while b > 1:
    for i in range(2 , b + 1):
        if b % i == 0:
            d.append(i)
            b = b // i
            break

print(d)    
"""

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