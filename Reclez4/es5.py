import calcolo
fig=input('Scegliere di quale figura geometrica si desidera ricavare la superficie: quadrato (1), rettangolo (2), cerchio (3) e triangolo rettangolo (4):')
if int(fig)==1:
  lato=input("Inserire il valore del lato:")
  print("L'area misura",calcolo.quad(float(lato)))
if int(fig)==2:
  lato1=input("Inserire il valore del primo lato:")
  lato2=input("Inserire il valore del secondo lato:")
  print("L'area misura",calcolo.rettangolo(float(lato1),float(lato2)))
if int(fig)==3:
  raggio=input("Inserire il valore del raggio:")
  print("L'area misura",calcolo.cerchio(float(raggio)))  
if int(fig)==4:
  cat1=input("Inserire il valore del primo cateto:")
  cat2=input("Inserire il valore del secondo cateto:")
  print("L'area misura",calcolo.tria(float(cat1),float(cat2)))