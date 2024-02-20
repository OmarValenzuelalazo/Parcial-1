diccionario={"casa":"hogar","coche":"carro","sueter":"sudadera","comida":"alimento"}
print(" Menu ")
print("1. Agregar elemento")
print("2. Modificar Elemento")
print("3. Borrar elemento")
print("4. Mostrar diccionario")
print("5. salir")
opcion = input("Ingresa opcion: ")

if opcion=="1":
    dato=input("ingrese dato")
    significado=input("ingrese significado")
    diccionario[dato]=significado
    print("elemento guardado")
if opcion=="4":
    for a in diccionario:
        print("elementos", a)
elif opcion == "3":
        dato = input("Ingresa dato a borrar: ")
        if dato in diccionario:
            diccionario.pop(dato)
            print("Elemento borrado")
if opcion == "2":
    dato = input("Ingresa dato a modificar: ")
    if dato in diccionario:
        nuevo_significado = input("Ingresa nuevo significado: ")
        diccionario[dato] = nuevo_significado
        print("Elemento modificado")