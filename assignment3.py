import math

n = int(input ("Enter the number of polygon points:"))

print("Enter x and y coordinates for polygon points:")
x = []
y = []

for i in range (n):
    row = input("Point {}: ".format(i+1))
    word = row.split()
    x.append(float(word[0]))
    y.append(float(word[1]))

x.append(x[0])
y.append(y[0])

print("Point    x       y")
print("--------------------")
for i in range (n): 
    print(i+1,":","   ",x[i],"   ",y[i])

#Ax
Ax = 0.0
for i in range (n):
    Ax = Ax + (x[i+1] + x[i]) * (y[i+1] - y[i])
Ax = 0.5 * Ax
print ("Ax = {:.2f}".format(Ax))

#Sx
Sx = 0.0
for i in range(n):
     Sx = Sx + (x[i+1] - x[i]) * (y[i+1]**2 + y[i] * y[i+1] + y[i]**2)
Sx = -1. / 6. * Sx
print ("Sx = {:.2f}".format(Sx))

#Sy
Sy = 0.0
for i in range(n):
        Sy = Sy + (y[i+1] - y[i]) * (x[i+1]**2 + x[i] * x[i+1] + x[i]**2)
Sy = 1. / 6. * Sy
print ("Sy = {:.2f}".format(Sy))

#Ix
Ix = 0.0
for i in range(n):
        Ix = Ix + (x[i+1] - x[i]) * (y[i+1]**3 + y[i+1]**2 * y[i] + y[i+1] * y[i]**2 + y[i]**3)
Ix = -1. / 12. * Ix
print ("Ix = {:.2f}".format(Ix))

#Iy
Iy = 0.0
for i in range(n):
        Iy = Iy + (y[i+1] - y[i]) * (x[i+1]**3 + x[i+1]**2 * x[i] + x[i+1] * x[i]**2 + x[i]**3)
Iy = 1. / 12. * Iy
print ("Iy = {:.2f}".format(Iy))

#Ixy
Ixy = 0.0
for i in range(n):
        Ixy = Ixy + (y[i+1] - y[i]) * (y[i+1] * (3 * x[i+1]**2 + 2 * x[i] * x[i+1] + x[i]**2) + y[i] * (3 * x[i]**2 + 2 * x[i] * x[i+1] + x[i+1]**2))
Ixy = -1. / 24. * Ixy
print ("Ixy = {:.2f}".format(Ixy))

#Xt
Xt = 0.0
Xt = Sy / Ax
print ("Xt = {:.2f}".format(Xt))

#Yt
Yt = 0.0
Yt = Sx / Ax
print ("Yt = {:.2f}".format(Yt))

#Ixt
Ixt = 0.0
Ixt = Ix - Yt**2 * Ax
print ("Ixt = {:.2f}".format(Ixt))

#Iyt
Iyt = 0.0
Iyt = Iy - Xt**2 * Ax
print ("Iyt = {:.2f}".format(Iyt))

#Ixyt
Ixyt = 0.0
Ixyt = Ixy + Xt * Yt * Ax
print ("Ixyt = {:.2f}".format(Ixyt))
