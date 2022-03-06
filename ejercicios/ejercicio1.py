import random
lista1=[]
lista2 = []
listafinal = []
lista_numero=[]
def crear_lista():
  lista_numero.sort()
  if len(lista_numero) < 20:
    numero=random.randint(0,100)
    lista_numero.append(numero)
    crear_lista()
  else:
    return lista_numero
crear_lista()
print(f"La lista inicial es: {lista_numero}")
cota_sup=len(lista_numero)
numero_medio=(cota_sup)// 2
def dicotomia(numero_medio):
  if numero_medio > 0:
    lista1.append(lista_numero.pop(numero_medio))
    dicotomia(numero_medio-1)
  if numero_medio == 0 and len(lista_numero) > 0:
    lista2.append(lista_numero.pop(numero_medio))
    dicotomia(numero_medio)
dicotomia(numero_medio)
listafinal=listafinal+ lista1 + lista2
print(f"La lista final con la dicotomía es {listafinal}")
  
