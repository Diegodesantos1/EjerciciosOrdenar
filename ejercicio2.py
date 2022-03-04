import random
lista_tareas= []
def crear_tareas():
  if len(lista_tareas) < 10:
    i = random.randint(1,100)
    j = random.randint(1,100)
    tarea =  (i,j)
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