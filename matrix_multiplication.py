from pprint import pprint

def matmul(A,B):
    row_a = len(A)
    col_a = len(A[0])
    row_b = len(B)
    col_b = len(B[0])
    
    if (col_a != row_b):
        print("Matrices not compatible to multiply.")
        return -1    
    
    C = [[0]*col_b for _ in range(row_a)]              #[0] * 3 → [0, 0, 0]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(row_b):
                C[i][j] += A[i][k]*B[k][j]

    return C

A = [
    [0,1],
    [1,0]
]

B = [
    [3],
    [8]
]

C = matmul(A,B)
for row in C:
    print(row)