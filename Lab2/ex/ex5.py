#Given a square matrix of characters writes a script that prints the string obtained by going
# through the matrix in spiral order (as in the example):

m = int(input("rows & columns: "))
a = []

for i in range(m):
    row =[]
    for j in range(m):
        row.append((input('A[' + str(i) + ',' + str(j) +']: ')))
    a.append(row)


def spiral_order(matrix):
    ans = [] # matricea retunata,
    if len(matrix) == 0:
        return ans
    l = len(matrix)
    seen = [[0 for _ in range(l)] for _ in range(l)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0
    # Iterate from 0 to R * C - 1
    for i in range(l * l):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if (0 <= cr and cr < l and 0 <= cc and cc < l and not (seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans


# Driver code
if __name__ == "__main__":
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    # Function call
    for x in spiral_order(a):
        print(x, end=" ")
    print()