# Write a program that accepts two complex numbers and outputs their sum and product.


import re

def parse_complex(s):
    s = s.replace(' ', '')
    match = re.match(r'^([+-]?[\d.]+)?([+-][\d.]+)?i$|^([+-]?[\d.]+)$', s)
    
    if not match:
        raise ValueError(f"Invalid complex number: {s}")
    
    if match.group(3):
        return (float(match.group(3)), 0.0)
    
    real = float(match.group(1)) if match.group(1) else 0.0
    imag = float(match.group(2)) if match.group(2) else 0.0
    
    return (real, imag)

def add_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1 + x2, y1 + y2)

def multiply_complex(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return (x1*x2 - y1*y2, x1*y2 + x2*y1)

def format_complex(c):
    a, b = c
    if b == 0:
        return f"{a}"
    elif b < 0:
        return f"{a} - {abs(b)}i"
    else:
        return f"{a} + {b}i"

c1 = parse_complex(input("Enter complex number 1 (e.g. 1+2i): "))
c2 = parse_complex(input("Enter complex number 2 (e.g. 3-4i): "))

print("Sum:", format_complex(add_complex(c1, c2)))
print("Product:", format_complex(multiply_complex(c1, c2)))