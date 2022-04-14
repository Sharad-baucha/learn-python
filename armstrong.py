num =  int(input("Enter a number"))
count = 0
temp1 = num
temp2 = num
sum = 0

while temp2 > 0:
    count += 1
    temp2 //= 10
print(count)

while num > 0:
    rem = num % 10
    sum = sum + rem ** count
    num = int(num / 10)

if sum == temp1:
    print("The given number is a Armstrong number")
else:
    print("The given number is not a Armstrong number")