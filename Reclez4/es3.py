print("Questo programma realizza il calcolo della legge oraria")
moto=input("Se vuoi il moto rett unif digita 1, se vuoi il moto rett unif accelerato digita 2 (nel SI):")
if int(moto)==1 :
  acc=0
elif int(moto)==2 :
  acc=input("Inserisci accelerazione: ")
vel=input("Inserisci velocità iniziale: ")
sp=input("Inserisci posizione iniziale: ")
tempo=input("Inserisci tempo: ")
if int(moto)==1:
  spazio=float(vel)*float(tempo)+float(sp)
  print("Lo spazio percorso è ",spazio)
elif int(moto)==2.:
  spazio=0.5*float(acc)*float(tempo)**2+float(vel)*float(tempo)+float(sp)
  print("Lo spazio percorso è ",spazio)
else:
  print("I dati inseriti non sono validi")

