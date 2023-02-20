def operaciones():
    apellidos = "jj"
    def resta(m, n):
        return m-n
    def suma(a, b):
        return a + b
    print("Operacion dentro de la funcion >> ",resta(654-321))

def main():
    x = int(input("Ingrese su primer numerito: "))
    y = int(input("Ingrese su segundo numerito: "))
    print(suma(x, y))
    pass

main()

# a, b, c = 10, 20, 30
#
# print(a,"-",b,"-",c)
#
# nombre = ""
#
# nombre = input("Ingrese su nombre: ")
# print("ingrese su edad: ")
# edad = int(input())
#
# print(nombre, "tiene:", (5*edad), "años") # Imprime valores separados
#
# print(nombre + " tiene:" , (5*edad),"años")  # Concatenar
#
