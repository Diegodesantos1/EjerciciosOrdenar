lista_palabra=["Alien","Eduardo","Cabeza","Rubén","Javier","Atlas","Río", "Servir", "Abrir","Camión", "Ordenador", "Mandaloriano", "Conflicto", "Móvil", "Estambul","Wifi", "Nft", "Real Madrid","Dicotomía","Gafas", "Pesado", "Bicicleta","Reloj", "Abrigo", "Criptoestafa", "Emblemático","Inanición","Comunicación","Ifema","Spa","Auditorio","Campo", "Bernabéu", "Iluminati", "Copiar", "Libre", "Como", "El", "Mar"]
print(lista_palabra)
cota_sup=len(lista_palabra)
numero_medio=(cota_sup)// 2
print("¿Qué palabra quieres buscar?")
palabra_buscar=str(input())
def dicotomia(numero_medio):
  numero_tabla =lista_palabra.index(palabra_buscar)
  if numero_tabla == numero_medio:
    print(f"La palabra {palabra_buscar} se encuentra en el índice {numero_tabla}")
  elif numero_tabla < numero_medio:
    dicotomia(numero_medio-1)
  elif numero_tabla > numero_medio:
    dicotomia(numero_medio+1)
dicotomia(numero_medio)
    