int1=5
int2=3
flt1=3.0
flt2=5.0
cpl1=4+6j
cpl2=2-4j
str1="Cammello"
str2="Orsetto"
bool1=True
bool2=False

print("-Operazioni tra oggetti")
print(int1+int2)
print(flt1*flt2)
print(cpl1-cpl2*cpl2)
print("C'era una volta un ",str1+" e un ",str2)
print("-Casting implicito")
int3=1
int3=int1/int2
print(int3)
int3=2022
print("Siamo nel ",int3)
print("-Casting esplicito")
print("Oggi è morto il ",str1," numero ",str(int1))
print(float(int1))
print("It's",str(bool1)," that ",int(flt2)," is larger than ",float(int2))
