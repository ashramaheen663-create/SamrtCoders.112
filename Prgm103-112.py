# LOOPS ADVANCED PATTERNS (NESTED LOGIC)
# BUTTERFLY PATTERN
N = 4
for i in range(1, N + 1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
for i in range(N, 0, -1):
    print("*" * i + " " * (2 * (N - i)) + "*" * i)
    # Hollow DIAMOND Inside RECTANGLE 
    N = 4
for i in range(N):
    print("*" * (N - i) + " " * (2 * i) + "*" * (N - i))
for i in range(N - 1, -1, -1):
    print("*" * (N - i) + " " * (2 * i) + "*" * (N - i))
    # NUMBER DIAMOND 
    N = 4
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    nums = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
    print(spaces + " ".join(nums))
for i in range(N - 1, 0, -1):
    spaces = "  " * (N - i)
    nums = [str(j) for j in range(1, i + 1)] + [str(j) for j in range(i - 1, 0, -1)]
    print(spaces + " ".join(nums))
# ZIG ZAG PATTERN 
cols = 9
for i in range(1, 4):
    row = ""
    for j in range(1, cols + 1):
        if ((i + j) % 4 == 0) or (i == 2 and j % 4 == 0):
            row += "*"
        else:
            row += " "
    print(row)
#SPIRAL NUMBER MATRIX 
N = 4
matrix = [[0] * N for _ in range(N)]
top, bottom, left, right = 0, N - 1, 0, N - 1
num = 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(" ".join(f"{val:2d}" for val in row))
# RIGHT ARROW PATTERN 
N = 4
for i in range(1, N + 1):
    print("  " * (i - 1) + "*" * i)
for i in range(N - 1, 0, -1):
    print("  " * (i - 1) + "*" * i)
# X Pattern 
N = 5
for i in range(N):
    for j in range(N):
        if i == j or i + j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# PLUS PATTERN 
N = 5
mid = N // 2
for i in range(N):
    for j in range(N):
        if i == mid or j == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# HEART SHAPE PATTERN 
 for r in range(6):
    for c in range(7):
        if (r == 0 and c % 3 != 0) or (r == 1 and c % 3 == 0) or (r - c == 2) or (r + c == 8):
            print("*", end="")
        else:
            print(" ", end="")
    print()
# SQUARE WITH DIAGONALS MARKED 
N = 5
for i in range(N):
    for j in range(N):
        if i == 0 or i == N - 1 or j == 0 or j == N - 1 or i == j or i + j == N - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
