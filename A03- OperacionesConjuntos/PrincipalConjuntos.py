def leerEntero
def menuPrincipal():
    print("********* Operaciones con conjuntos  *********")
    print(" 0- Salir")
    print(" 1- Union")
    print(" 2- Interseccion")
    print(" 3- Diferencia")
    print(" 4- Diferencia Simétrica")
    return int(input("     >>> Ingrese una opcion: "))

def leerConjunto():
    conj = []
    numElementos = int(input("  Ingrese el numero de elementos: "))

    for ...
        conj[  ] = ....|
    return  conj

def unir( conj1, conj2 ):
    union = []
    ...
    return union

def diferencia( conj1, conj2 ):
    difer = []
    ...
    return difer

def diferenciaSimétrica( conj1, conj2 ):
    diferSim = []
    ...
    return diferSim

def interseccion( conj1, conj2 ):
    inter = []
    ...
    return inter
def main():
    conj1 = leerConjunto()
    conj2 = leerConjunto()
    while (  ):
        opcion = menuPrincipal()
        match( opcion ):
            case 0:
                print(" Adios, vuelve pronto. ")
            case 1:
                print(" Vamos a unir conjuntos ")
            case 2:
                print(" Vamos a Intersecatar conjuntos ")
            case 3:
                print(" Vamos a hacer una diferencia de conjuntos ")
            case 4:
                print(" Vamos a hacer una diferencia de conjuntos ")
            else:
                print(" Error: pcion inválida.")

main()



