from complex_nos import *

# Matrix with complex entries
M = [[(1,2), (3,-1)],
     [(0,4), (2,2)]]

def add_complex_matrices(M1, M2):
    row1 = len(M1)
    col1 = len(M1[0])
    row2 = len(M2)
    col2 = len(M2[0])

    if not(row1 == row2 and col1 == col2):
        return
    M = [[(0,0)]*col1 for _ in range(row1)]
    for i in range(row1):
        for j in range(col1):
            c1 = M1[i][j]
            c2 = M2[i][j]
            M[i][j] = add_complex(c1,c2)
    return M

def scalar_multiply_matrix(M, k):
    M_new = [[(0,0)]*len(M[0]) for _ in range(len(M))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            M_new[i][j] = multiply_complex(M[i][j], k)
    return M_new

def additive_inverse_matrix(M):
    return scalar_multiply_matrix(M, (-1,0))


def multiply_complex_matrices(A,B):
    row_a = len(A)
    col_a = len(A[0])
    row_b = len(B)
    col_b = len(B[0])

    if (col_a != row_b):
        print("Matrices not compatible to multiply.")
        return
    
    C = [[(0,0)]*col_b for _ in range(row_a)] 

    for i in range(row_a):
        for j in range(col_b):
            elem = (0,0)
            for k in range(col_a):
                elem = add_complex(elem, multiply_complex(A[i][k], B[k][j]))
            C[i][j] = elem  

    return C

def conjugate_transpose_complex_matrix(M):
    m = len(M)
    n = len(M[0])

    C = [[(0,0)]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            (a,b) = M[j][i]
            C[i][j] = (a,-b)

    return C

