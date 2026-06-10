'''
this program can do the following:
add 2 complex nos.
subtract 2 complex nos. 
multiply 2 complex nos.
divide 2 complex nos.
calculate the modulus and conjugate of a complex no,
'''



from math import sqrt



def add_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1 + x2, y1 + y2)


def sub_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1 - x2, y1 - y2)


def multiply_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1*x2 - y1*y2, x1*y2 + x2*y1)


def divide_complex(a,b):
    c = conjugate_complex(b)
    (p,q) = multiply_complex(a,c)
    mod_sq = modulus_complex(b)**2
    return (p/mod_sq, q/mod_sq)


def modulus_complex(a):
    (x1,x2) = a
    return sqrt(x1*x1 + x2*x2)


def conjugate_complex(a):
    (x1,x2) = a
    return (x1, -x2)



