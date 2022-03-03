lista_palabra=["Alien","Eduardo","Cabeza","Rubén","Javier","Atlas","Río", "Servir", "Abrir","Camión", "Ordenador", "Mandaloriano", "Conflicto", "Móvil", "Estambul","Wifi", "Nft", "Real Madrid","Dicotomía","Gafas", "Pesado", "Bicicleta","Reloj", "Abrigo", "Criptoestafa", "Emblemático","Inanición","Comunicación","Ifema","Spa","Auditorio","Campo", "Bernabéu", "Iluminati", "Copiar", "Libre", "Como", "El", "Mar"]
lista_dicotomia=[]
print(lista_palabra)
cota_sup=len(lista_palabra)
numero_medio=(cota_sup)// 2
def dicotomia(numero_medio):
  lista_dicotomia.append(lista_palabra.pop(numero_medio))
  dicotomia(numero_medio-1)
dicotomia(numero_medio)
print(f"La lista final es: {lista_dicotomia}")
    