# Create a 2D - List
matrix = [[1 , "Shivani ", 29], [2 , "Dnyanada", 27 , "Vakil"], [1 , "Jai ", 36]]
print(matrix)

# Number of rows
print(len(matrix))
      
# Number of columns
print(len(matrix[1]))

# Take an input for a matrix and print the elements 

rows = int(input("Enter the number of rows - "))
columns = int(input("Enter the number of columns - "))

marks = []

for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Enter your element - "))
        temp.append(x)
    marks.append(temp)

for i in range(rows):
    for j in range(columns):
        print(marks[i][j], end = " ")
    print("\n")
