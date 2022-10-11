#Given a square matrix of characters writes a script that prints the string obtained by going
# through the matrix in spiral order (as in the example):

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

def spiral_matrix_print(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row - 1
    left = 0
    right = col - 1

    direction = 0

    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):  # moving left->right
                print(arr[top][i], end=" ")

            top += 1
            direction = 1

        elif direction == 1:
            for i in range(top, bottom + 1):  # moving top->bottom
                print(arr[i][right], end=" ")

            right -= 1
            direction = 2

        elif direction == 2:
            for i in range(right, left - 1, -1):  # moving right->left
                print(arr[bottom][i], end=" ")

            bottom -= 1
            direction = 3

        elif direction == 3:
            for i in range(bottom, top - 1, -1):  # moving bottom->top
                print(arr[i][left], end=" ")
            left += 1
            direction = 0

spiral_matrix_print(R,C, matrix)