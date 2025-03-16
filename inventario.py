import sys

# inicializacion del inventario
inventario = {}

# definimos las funciones
# agregar producto
def agregar_producto():
    key = input("ingrese producto ")
    valor = int(input("ingrese cantidad "))

    # si no se encuentra se agrega directamente
    if key not in inventario:
        inventario[key] = valor

    # si se encuentra se pregunta si quiere sumar su cantidad
    else:
        print ("el producto ya se encuentra, quieres sumar su cantidad? y/n")
        if (input() == "y"):
            inventario[key]+=valor
        else:
            print("volviendo al menu...")

# eliminar producto
def eliminar_producto():
    key = input("ingrese producto a eliminar ")
    # si esta el producto se elimina
    if key in inventario:
        del inventario[key]
    else:
        print("no se encuentra el producto")
        print("volviendo al menu...")

# mostrar inventario 
def mostrar_inventario():
    print("     Inventario      ")
    print(inventario)

# salir del programa
def salir():
    print("saliendo...")
    sys.exit(0)

while True:
    print()
    print("     Menu      ")
    print("1. agregar producto")
    print("2. eliminar producto")
    print("3. mostrar inventario")
    print("4. salir")

    match input("elije una opcion: "):
        case "1":
            print()
            agregar_producto()
        case "2":
            print()
            eliminar_producto()
        case "3":
            print()
            mostrar_inventario()
        case "4":
            print()
            salir()

