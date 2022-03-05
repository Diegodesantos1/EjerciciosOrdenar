import random
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
    
    
