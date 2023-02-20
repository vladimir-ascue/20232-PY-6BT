# Declaracion y asignacion multiple
# nombre, apellido, correo = "Vladimir", "Ascue", "vladimir.ascue@gmail.com"
#
# print("nombre:" + nombre)
# print("apellido:" + apellido)
# print("correo:" + correo)

# Recordemos que la coma (,) determinar variables diferentes (independientes)
def mostrar1(): # METODOS: (Procedimientos) no retornan valores
    # print: puede recibir varios valores separados por comas (,) >> Listas
    print("Vladimir", "Ascue" + " Lovon")

def mostrar2(): # METODOS: Funciones no retornan valores
    # Las funciones pueden retornar varios valores separados por comas (,) >> Listas
    return "Vladimir", "Ascue" + " Lovon"

def sumar(a, b):
    return a + b

# Nome === null
print( mostrar2() )

print( mostrar2()[0] )
print( mostrar2()[1] )

print("*************")

for item in mostrar2():
    print(item)

print(sumar(int(input("Ingrese Num1:")),int(input("Ingrese Num2:"))))

