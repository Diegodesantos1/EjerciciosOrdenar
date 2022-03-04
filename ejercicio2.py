import random

lista_tareas = []
def crear_tareas():
  if len(lista_tareas) < 5:
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
def nombrar_tareas():
  tareas =["Fregar", "Aspirar", "Poner la lavadora", "Hacer la comida", "Limpiar los baños", "Tender la ropa", "Limpiar el polvo","Recoger la habitación", "Ordenar las estanterías", "Sacar el lavavajillas"]
  numero_tareas = random.randint(1,10)
  tarea_escrita=tareas.pop(numero_tareas)
  tarea_numero = lista_tareas.pop(0)
  diccionario={tarea_escrita: tarea_numero}
  print(diccionario)
nombrar_tareas()