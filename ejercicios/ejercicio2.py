import random

lista_tareas = []
def crear_tareas():
  if len(lista_tareas) < 10:
    i = random.randint(1,10)
    j = random.randint(1,10)
    if i >= j:
      crear_tareas()
    else:
      tarea = f"{i,j}"
      lista_tareas.append(tarea)
      crear_tareas()
  else:
    return lista_tareas
crear_tareas()
print(lista_tareas)

def ordenar_tareas():
  lista_tareas.sort()
  print(lista_tareas)
ordenar_tareas()

tareas =["Fregar", "Aspirar", "Poner la lavadora", "Hacer la comida", "Limpiar los baños", "Tender la ropa", "Limpiar el polvo","Recoger la habitación", "Ordenar las estanterías", "Sacar el lavavajillas"]
diccionario = {}
def nombrar_tareas():
  if len(tareas) != 0 or len(lista_tareas) != 0:
    numero_random = random.randint(0,len(tareas) - 1)
    tarea_escrita=tareas.pop(numero_random)
    tarea_numero = lista_tareas.pop(0)
    diccionario[tarea_escrita] = tarea_numero
    nombrar_tareas()
  else:
    print(diccionario)
    lista_tareas_ordenada=diccionario.keys()
    print(f"Las tareas son en orden de prioridad: {lista_tareas_ordenada}")
nombrar_tareas()
