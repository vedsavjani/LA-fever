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

# def matmul(A,B):
    # row_a = len(A)
    # col_a = len(A[0])
    # row_b = len(B)
    # col_b = len(B[0])
    
    # if (col_a != row_b):
    #     print("Matrices not compatible to multiply.")
    #     return -1    
    
    # C = [[0]*col_b for _ in range(row_a)]              #[0] * 3 → [0, 0, 0]

#     for i in range(row_a):
#         for j in range(col_b):
#             for k in range(row_b):
#                 C[i][j] += A[i][k]*B[k][j]

#     return C

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


M1 = [[(1,2), (3,-1)],
      [(0,4), (2,2)]]

M2 = [[(1,-2), (-3,1)],
      [(0,-4), (-2,-2)]]

print(add_complex_matrices(M1, M2))    # expect [[(2,0),(0,0)],[(0,0),(0,0)]]
print(additive_inverse_matrix(M1))     # expect [[(-1,-2),(-3,1)],[(0,-4),(-2,-2)]]
print(scalar_multiply_matrix(M1, (0,1)))  # multiply by i: expect [[(-2,1),(-1,-3)],[(-4,0),(-2,2)]]

A = [[(1,0), (0,1)],
     [(0,1), (1,0)]]

B = [[(1,0), (0,1)],
     [(0,1), (1,0)]]

print(multiply_complex_matrices(A, B))
# expect [[(0,0),(0,2)],[(0,2),(0,0)]]
# because (1+0i)(1+0i) + (0+1i)(0+1i) = 1 + (-1) = 0