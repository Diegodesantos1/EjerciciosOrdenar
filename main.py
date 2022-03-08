def eleccion_ejercicio():
  variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))
  if variable == 1:
      from ejercicios import ejercicio1
  elif variable == 2:
      from ejercicios import ejercicio2
  elif variable == 3:
      from ejercicios import ejercicio3
  else:
      eleccion_ejercicio()
eleccion_ejercicio()