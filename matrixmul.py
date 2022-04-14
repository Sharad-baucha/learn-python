x = int(input("Enter the Number of rows of first matrix : " ))
y = int(input("Enter the Number of Columns of first matrix: "))

m = int(input("Enter the Number of rows of second matrix: " ))
n = int(input("Enter the Number of Columns of second matrix: "))

if(y != m):
    print("The matrix multiplication cannot be performed")

# Initialize matrix
matrix_a = []
matrix_b = []

print("Enter the elements of 1st Matrix :")
  
# For user input
for i in range(x):          # A for loop for row entries
    a =[]
    for j in range(y):      # A for loop for column entries
         a.append(int(input()))
    matrix_a.append(a)
  
# For printing the matrix
for i in range(x):
    for j in range(y):
        print(matrix_a[i][j], end = " ")
    print()

print("Enter the elements of 2nd Matrix :")
  
# For user input
for i in range(m):          # A for loop for row entries
    b =[]
    for j in range(n):      # A for loop for column entries
         b.append(int(input()))
    matrix_b.append(b)
  
# For printing the matrix
for i in range(m):
    for j in range(n):
        print(matrix_b[i][j], end = " ")
    print()

301059767