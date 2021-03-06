<h1 align="center">Ejercicios de Ordenar</h1>

*He usado la herramienta de Replit para poder programar online y así resolver los ejercicios propuestos aplicando el contenido de esta lección, que es ordenar, los ejercicios han sido realizados bajo mi interpretación de los enunciados*

***

<h2>Repositorio</h2>

Este es el link del [Repositorio](https://github.com/Diegodesantos1/EjerciciosOrdenar)

## Ejercicio 1: Ordenación por inserción dicotómica

*En este ejercicio he creado una lista aleatoria en función de la longitud e intervalo asignado, una vez creada la lista, se ordena uno a uno los elementos, se aplica la dicotomía y se printea la lista final*

***

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosOrdenar/milestone/1?closed=1)

[Flowchart](https://github.com/Diegodesantos1/EjerciciosOrdenar/blob/main/Flowcharts/Flow_Ejercicio1/Flowchart_1.drawio) en formato XML

![image](https://user-images.githubusercontent.com/91721855/157729166-f422e175-406b-45db-800e-5d4ba5856ea6.png)

El código empleado para resolverlo es el siguiente:

```python
import random

lista_numero= []
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

def ordenarlista_dicotomia(lista_numero):
  for i in range(len(lista_numero)):
    for j in range(i, len(lista_numero)):
      if lista_numero[i] > lista_numero[j]:
        lista_numero[i], lista_numero[j] = lista_numero[j], lista_numero[i]
  print(f"La lista ordenada con una sola tabla es esta: \n {lista_numero}")
ordenarlista_dicotomia(lista_numero)
    
lista1= []
lista2 = []
listafinal = []
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
print(f"\n La lista final con dicotomía es: \n {listafinal}")
```

## Ejercicio 2: Una ordenación topológica

*En este ejercicio, el algoritmo crea una lista de tareas aleatoria en función de "(i, j)" y la ordena, después le asigna aleatoriamente una tarea escrita como "Fregar" o "Barrer" y con esto crea un diccionario y una vez creado printea la solución en orden de prioridad de lass tareas*

***

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosOrdenar/milestone/2?closed=1)

[Flowchart](https://github.com/Diegodesantos1/EjerciciosOrdenar/blob/main/Flowcharts/Flow_Ejercicio2/Ejercicio2.drawio) en formato XML

![image](https://user-images.githubusercontent.com/91721855/157729841-980f4413-2f9e-4801-8c45-6c0476cbf913.png)

El código empleado para resolverlo es el siguiente:

```python
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
print(f"{lista_tareas}\n")

def ordenar_tareas():
  lista_tareas.sort()
  print(f"{lista_tareas}\n")
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
    
    print(f"{diccionario}\n")
    lista_tareas_ordenada=diccionario.keys()
    print(f"Las tareas son en orden de prioridad: {lista_tareas_ordenada}")
nombrar_tareas()
```

## Ejercicio 3: Completar las especificaciones

*En este ejercicio, el algoritmo crea una lista aleatoria en función de la longitud y el intervalo, y con esto crea segmentos de números decrecientes, y cuando uno es superior al siguiente coloca un separador "||"*

***

Aquí su [Milestone](https://github.com/Diegodesantos1/EjerciciosOrdenar/milestone/3?closed=1)

[Flowchart](https://github.com/Diegodesantos1/EjerciciosOrdenar/blob/main/Flowcharts/Flow_Ejercicio3/Ejercicio3.drawio) en formato XML

![image](https://user-images.githubusercontent.com/91721855/157729906-44188617-ca88-4b17-b7e5-dbcc94e25e6a.png)


El código empleado para resolverlo es el siguiente:

```python
import randint
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

print(f"La lista inicial es:\n {lista_numero}\n")

def crear_segmentos():
  num=lista_numero.pop(0)
  lista_segmento.append(num)
  while len(lista_numero) != 0:
    n=0
    if lista_segmento[len(lista_segmento)-1] >= lista_numero[n]:
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    elif lista_segmento[len(lista_segmento)-1] <= lista_numero[n]:
      lista_segmento.append("||")
      numero=lista_numero.pop(n)
      lista_segmento.append(numero)
    else:
      break
crear_segmentos()

num_segmento=lista_segmento.count("||")
num_segmento= num_segmento + 1
print(f"la lista final es:\n {lista_segmento} \n Tiene {num_segmento} segmentos")
```
