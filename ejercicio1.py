lista_palabra=["Alien","Eduardo","Cabeza","Rubén","Javier","Atlas","Río", "Servir", "Abrir"]
lista1=[]
lista2 = []
listafinal = []
print(lista_palabra)
cota_sup=len(lista_palabra)
numero_medio=(cota_sup)// 2
def dicotomia(numero_medio):
  if numero_medio > 0:
    lista1.append(lista_palabra.pop(numero_medio))
    dicotomia(numero_medio-1)
  if numero_medio == 0 and len(lista_palabra) > 0:
    lista2.append(lista_palabra.pop(numero_medio))
    dicotomia(numero_medio)
dicotomia(numero_medio)
lista1_reversed=(lista1[::-1]) #copiado de stackoverflow, ya que el reverse() no me funcionaba
listafinal.append(lista1.pop(0))
listafinal=listafinal+ lista1_reversed + lista2
print(f"La lista final es {listafinal}")