num = int(input("Enter a number:"))
temp = num
sum = 0

while num > 0:
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10

if sum == temp:
    print(temp ,"is a palindrome number")
else:
    print(temp, "is not a palindrome number")