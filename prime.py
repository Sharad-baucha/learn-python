num = input("enter a number")
num = int(num)

i=1
count=0
while i<=num:
    if(num%i==0):
        count=count+1
    i=i+1

if count<=2:
    print("Number is prime")
else:
    print("Number is not prime")