import random
lista_numero=[]
lista_segmento=[]
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
  if lista_numero[posicion_numero_max] > lista_numero[posicion_numero_max + 1]:
    lista_segmento.append(lista_numero.pop(posicion_numero_max))
    lista_segmento.append(lista_numero.pop(posicion_numero_max + 1))
    print(lista_segmento)
    crear_segmentos(posicion_numero_max + 1)
  else:
      return (lista_segmento)
crear_segmentos(posicion_numero_max)
  