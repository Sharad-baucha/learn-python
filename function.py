def addNumbers(num1, num2):
    return num1+num2

sum = addNumbers(6,9)
#print(sum)
#print(addNumbers(num2=3, num1=1))

# def factorial()
# def addNumbers(num1, *num2):
#     print(type(num2))
#     sum = num1
#     for num in num2:
#         sum += num
#     return sum
    
# print(addNumbers(2,6,7,8,9))
# num1 = 6
# num2 = 9
# sum = lambda num1,num2 : num1+num2 
# print(sum(6,9))

# nums = [i for i in range(1,21) if i%2==0]
# print(nums)

# nums = [i for i in range(1,21)]
# print(nums)
# evenNumbers = list(filter(lambda num : num %2 ==0 , nums))
# print(evenNumbers)

# numbers = list(map(lambda num : num * 2, nums))
# print(numbers)

vowel_list = ['a','e','i','o','u']
new_list = ['apple','yogesh','sharad','otu','aashish']
vowel = list(filter(lambda str1 : str1[0] in vowel_list , new_list))
print(vowel)