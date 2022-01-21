"""
a=[23,432,52,65,24,64,24]
if(23 in a):
    print(a[1])
import math  
if(8*3 in a):
  print(math.pi)   
ba=range(1,10,2)
ab=[el*math.pi for el in ba]  
print(ab)
l1=[1,2]
l2=['a','b']
l3=['e',5]
l4=[(e1,e2,e3) for e1 in l1 for e2 in l2 for e3 in l3]
print(l4)
"""
"""
import time
g=list(range(10000000))
h=list(range(1000000))
t1=time.perf_counter()
g.extend(h)
t2=time.perf_counter()
print(t2-t1)

t1=time.perf_counter()
g+h
t2=time.perf_counter()
print(t2-t1)

t1=time.perf_counter()
g.append(h)
t2=time.perf_counter()
print(t2-t1)
"""
"""
lista=[1, 2, 3, 4]
print("Lista iniziale : ",lista)
for i in range(5,7):
  lista.append(i)
print ("Append: ", lista)
lista.pop()
print ("Pop: " , lista.pop())
"""
"""
l=[1,2]
l2=['a','b']
l3=[4,5]
f=[]
for e1 in l:
  for e2 in l2:
    for e3 in l3:
      f.append((e1,e2,e3))
"""
"""
squares = {1:1, 2:4, 3:9, 4:16, 5:25}
print(squares) 
print(squares.popitem())
print(squares)      
for i in squares:
  print(squares[i])

for item in squares: 
  if 16 in squares[item]:
   del squares
"""
"""
i=0
while i<18:
  i=i+1
  if(i>10):
    break
  print(i) 
"""
"""
while True:
  s = input('Enter something : ')
  print('Length of the string is', len(s))
  if s == 'quit':
    break  
  else:
    print("Picciotto cambia parola")
"""

a={1:'kaboom',2:'evviva',3:'islanda',4:'gabbiano'}
for el in a:
  print(a[el])
  if a[el]=='islanda':
    print(a[el])
    break

for n in range(4):
  print(n)
      