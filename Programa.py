

def S(a, b):
    return a + b
def M(a, b):
    return a * b
def D (a, b):
    return  a / b
def R(a, b):
     return a - b
while True:
    print("*** Menu principal***")
    print("1. sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4.Division")
    opc= input("ingrese una opcion")
    n1 = float(input("Numero 1:"))
    n2 = float(input("Numero 2:"))
    if opc=="1":
        print("la suma es: ",S(n1, n2))
    elif opc=="2":
        print("la resta es:" ,R(n1,n2))
    elif opc=="3":
        print("la multiplicacion es: ",M(n1, n2))
    elif opc=="4":
        print("la division es: ",D(n1, n2))
    else:
        print("opcion invalida")










