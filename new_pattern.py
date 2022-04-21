# k = 65
# for i in range(1 , 6 , 1):
    
#     for j in range(1 , 6 , 1):
        
#         if j <= i:
#             print(chr(k), end=" ")
        
#     print()
#     k += 1


for i in range(1 , 6 , 1):
    
    for j in range(1 , 10 , 1):
        
        if (j >= 6 - i and j <= 4 + i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
        
    print()
