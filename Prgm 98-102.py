# LOOPS: ALPHABET PATTERNS 
#Alphabet triangle (row repeat)
N = 4
for i in range(N):
    ch = chr(ord('A') + i)
    print(" ".join([ch] * (i + 1)))
#Alphabet triangle (sequential) 
N = 4
for i in range(1, N + 1):
    print(" ".join(chr(ord('A') + j) for j in range(i)))
#Reverse alphabet triangle
N = 4
for i in range(N, 0, -1):
    print(" ".join(chr(ord('A') + j) for j in range(i)))
#Right-aligned alphabet triangle
N = 4
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    left = [chr(ord('A') + j) for j in range(i)]
    right = [chr(ord('A') + j) for j in range(i - 2, -1, -1)]
    print(spaces + " ".join(left + right))
#Alphabet pyramid (centered)  
N = 4
for i in range(1, N + 1):
    spaces = "  " * (N - i)
    left = [chr(ord('A') + j) for j in range(i)]
    right = [chr(ord('A') + j) for j in range(i - 2, -1, -1)]
    print(spaces + " ".join(left + right))
