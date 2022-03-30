def f_sum(a, b):
  sum = a + b    
  return sum
a = 1
b = 2
sum = 3
f_sum(100, 100)
print(sum)

def f_sum(a, b):
  sum = a + b
  return sum
a = 1
b = 2
sum = 3
print(f_sum(100, 100))

'''Questo accade perchè la variabile sum è definita sia globalmente (fuori dalla funzione) che localmente (all'interno della funzione stessa): la variabile ha valore 200 solamente all'interno della funzione stessa dunque, nel primo caso, quello che si va a stampare è il valore che la variabile ha nel programma "globale" che risulta dunque essere 3. Nel secondo caso, invece, si va a stampare esattamente il valore della variabil all'interno della funzione e questo restituisce il valore 200. '''