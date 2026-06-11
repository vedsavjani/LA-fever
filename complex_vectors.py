from complex_nos import *
from complex_matrices import *


def scalar_multiply_vector(v, k): #the scalar can be a complex no. as well
    lis = []
    for c_i in v:
        lis.append(multiply_complex(c_i,k))        
    return lis

def add_complex_vectors(v1,v2):
    if (len(v1) != len(v2)): 
        return
    n = len(v1)
    lis = []
    for i in range(n):
        (a1,b1) = v1[i]
        (a2,b2) = v2[i]
        lis.append((a1+a2, b1+b2))
    return lis

def sub_complex_vectors(v1,v2):
    if (len(v1) != len(v2)): 
        return
    n = len(v1)
    lis = []
    for i in range(n):
        (a1,b1) = v1[i]
        (a2,b2) = v2[i]
        lis.append((a1-a2, b1-b2))
    return lis

def additive_inverse_vector(v):
    return scalar_multiply_vector(v,(-1,0))


def inner_product_vectors(v1,v2):
    total = (0,0)

    for i in range(len(v1)):
        cong_v1_i = conjugate_complex(v1[i])
        total = add_complex(total, multiply_complex(cong_v1_i, v2[i]))
    return total


def norm_complex_vector(v):
    c = inner_product_vectors(v,v)
    (a,b) = c
    return sqrt(a)


def dist_bw_complex_vectors(v1,v2):
    v = sub_complex_vectors(v1,v2)
    return norm_complex_vector(v)

v1 = [(1,0), (0,1)]
v2 = [(0,1), (1,0)]

print(inner_product_vectors(v1, v2))    # expect (0,2) — not real, vectors not orthogonal
print(inner_product_vectors(v1, v1))    # expect (2,0) — always real
print(norm_complex_vector(v1))          # expect 1.414...
print(dist_bw_complex_vectors(v1, v2)) # expect 2.0