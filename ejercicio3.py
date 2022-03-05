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

def crear_segmentos():
  numero_max = max(lista_numero)
  posicion_numero_max =(lista_numero.index(numero_max))
  while len(lista_numero):
    if lista_numero[posicion_numero_max] < lista_numero[posicion_numero_max + 1]:
      lista_segmento.append(lista_numero[posicion_numero_max + 1])
    else:
      return (lista_segmento)
crear_segmentos()
  
print(lista_segmento)