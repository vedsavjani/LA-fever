from complex_nos import *
import matplotlib.pyplot as plt

#this program can tranform a set of points on a complex plan by multiplying a complex number to them

points = []
n = int(input("Enter number of points: "))
for i in range(n):
    x = float(input(f"Point {i+1} x: "))
    y = float(input(f"Point {i+1} y: "))
    points.append((x, y))


xi_old = []
yi_old = []
for point in points:
    (x,y) = point
    xi_old.append(x)
    yi_old.append(y)

plt.plot(xi_old, yi_old)
plt.show()

# def multiply_complex(a, b):
#     (x1, y1) = a
#     (x2, y2) = b
#     return (x1*x2 - y1*y2, x1*y2 + x2*y1)

a = int(input("Enter real part: "))
b = int(input("Enter imaginary part: "))
c_num = (a,b)

xi_new = []
yi_new = []
for point in points:
    c = multiply_complex(c_num, point)
    (x,y) = c
    xi_new.append(x)
    yi_new.append(y)

plt.plot(xi_new,yi_new)
plt.show()
