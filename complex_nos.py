'''
this program can do the following:
1. add 2 complex nos.
2. subtract 2 complex nos. 
3. multiply 2 complex nos.
4. divide 2 complex nos.
5. calculate the modulus and conjugate of a complex no.
6. convert cartesian to polar coordinates and vise versa
'''



from math import *

#######################################################################

def add_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1 + x2, y1 + y2)


#######################################################################
def sub_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1 - x2, y1 - y2)



#######################################################################
def multiply_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1*x2 - y1*y2, x1*y2 + x2*y1)


#######################################################################
def divide_complex(a,b):
    c = conjugate_complex(b)
    (p,q) = multiply_complex(a,c)
    mod_sq = modulus_complex(b)**2
    return (p/mod_sq, q/mod_sq)


#######################################################################
def modulus_complex(a):
    (x1,x2) = a
    return sqrt(x1*x1 + x2*x2)


#######################################################################
def conjugate_complex(a):
    (x1,x2) = a
    return (x1, -x2)


#######################################################################
def cartesian_polar(C):
    (a,b) = C
    r = modulus_complex(C)
    theta = atan2(b, a)  #gives theta in radians
    return (r,theta)


#######################################################################
def polar_to_cartesian(P):
    (r, theta) = P
    a = r * cos(theta)
    b = r * sin(theta)
    return (a,b)


