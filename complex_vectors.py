from complex_nos import multiply_complex



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

def additive_inverse_vector(v):
    return scalar_multiply_vector(v,(-1,0))

#3d complex vectors
v1 = [(1,2), (3,-1), (0,4)] 
v2 = [(1,-2), (-3,1), (0,-4)]

print(add_complex_vectors(v1, v2))      # expect [(2,0), (0,0), (0,0)]
print(additive_inverse_vector(v1))             # expect [(-1,-2), (-3,1), (0,-4)]
print(scalar_multiply_vector(v1, (0,1)))       # multiply by i: expect [(-2,1), (1,3), (-4,0)]