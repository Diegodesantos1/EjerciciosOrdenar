import random
lista_numero=[]
lista_segmento = []
def crear_lista():
  if len(lista_numero) < 20:
    numero=random.randint(0,100)
    lista_numero.append(numero)
    crear_lista()
  else:
    return lista_numero
crear_lista()
print(f"La lista inicial es: {lista_numero}")
posicion_numero_max = lista_numero.index(max(lista_numero))
def crear_segmentos(posicion_numero_max):
  lista_numero.append([0])
  while len(lista_numero):
    for n in range (len(lista_numero)- 1):
      if lista_numero[n] > lista_numero[n+1]:
        lista_numero.append(lista_numero[n])
      else:
        lista_numero.append("//}")
crear_segmentos(posicion_numero_max)
print(lista_numero)