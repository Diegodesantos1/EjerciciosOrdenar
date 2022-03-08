import random
lista1=[]
lista2 = []
listafinal = []
lista_numero=[]
print("¿Qué longitud quieres que tenga la lista?")
longitud_lista=int(input())
print("Establece el intervalo inferior")
inf=int(input())
print("Establece el intervalo superior")
sup=int(input())

def crear_lista():
  if len(lista_numero) < longitud_lista:
    numero=random.randint(inf,sup)
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
  
