import random
lista_numero=[]
lista_segmento = []
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

def crear_segmentos():
  num=lista_numero.pop(0)
  lista_segmento.append(num)
  while len(lista_numero) != 0:
    n=0
    if lista_segmento[len(lista_segmento)-1] >= lista_numero[n]:
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    elif lista_segmento[len(lista_segmento)-1] <= lista_numero[n]:
      lista_segmento.append("//")
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    else:
      break
crear_segmentos()

num_segmento=lista_segmento.count("//")
num_segmento= num_segmento + 1
print(f"la lista final es {lista_segmento} y tiene {num_segmento} segmentos")