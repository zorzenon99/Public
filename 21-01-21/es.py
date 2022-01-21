import math 
import numpy as np

print(math.pi)
"""
def f_vect(x):
    x1 = 3
    x2 = 5
    return(x<10, x1, x2)

print(f_vect(12))  

b=np.array([5,6,7,8])
c=np.arange(1,5)
d=c+b
print("Somma (b)=" ,b,"+(c)=",c, "= ", b+c)
b+=1
print("Aumenta b di 1: b=", b)
print("Moltiplica c*3 " ,c, "* 3= ",c*3)
print("Seno(c)", np.sin(c))

a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
print(a[0][0])
print(a[2])
print(a[:,1])
print(a[2:,1:3])

print("Cambio")
a=np.arange(25)
a=a.reshape((5,5)) 
print(a)
print(a[::,1])
print(a[1,10::-1])
"""
a = np.arange(10)
b = np.zeros_like(a) 
print(b)  
b[:] = a[:]       
b[3] = 500
b == a
print(a)
print(b)