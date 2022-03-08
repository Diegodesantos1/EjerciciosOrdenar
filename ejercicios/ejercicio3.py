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
def crear_segmentos():
  num=lista_numero.pop(0)
  lista_segmento.append(num)
  while len(lista_numero)-2:
    n=0
    if lista_segmento[len(lista_segmento)-1] > lista_numero[n]:
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    elif lista_segmento[len(lista_segmento)-1] < lista_numero[n]:
      lista_segmento.append("//")
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    else:
      break
crear_segmentos()
print(f"la lista con segmentos es {lista_segmento}")