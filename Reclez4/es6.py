#Le funzioni di introspezione hanno lo scopo di permettere al programmatore di avere delle informazioni sul codice stesso.
#La funzione dir permette di ricercare all'interno di un modulo le varie funzione definite in base al nome.
import calcolo
import math
print(dir(calcolo))
#La funzione help fornisce tutto il materiale relativo alle descrizione di una data funzione.
print()
print(dir(math.gamma))

"""La funzione type, infine, restituisce il "tipo" dell'oggetto che viene messo come argomento (int, float, bool, ecc"...)."""


a=1
b=2.3
c=True
d=(4,5,6)
e=[3,5.6,"mucca"]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))