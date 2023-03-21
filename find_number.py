import sys

from termcolor import colored

list = [3, 4, 3, 1, 5, 8, 1, 2, 5, 4, 0, 8, 9, 4, 3, 9, 7, 8, 4, 3, 5, 4, 0, 3, 8, 9, 5, 4, 3, 9, 3, 8, 0, 9, 3, 5, 1]


def print_menu():
    opc = 0
    while opc != 9:
        print("\n")
        print(colored("**********MENU DE OPCIONES**********",'green',attrs=['bold']))
        print(colored("1) Usar Lista Predeterminada",'green'))
        print(colored("2) Usar Lista nueva",'green'))
        print(colored("9) SALIR",'yellow'))
        opc = int(input("Ingrese su opcion: "))
        if opc == 1:
            usar_lista_hecha()
        elif opc == 2:
            nueva_lista()
        elif opc == 9:
            sys.exit()
        else:
            print(colored("ERROR!! Opción invalida. Reintente", 'red', attrs=['bold', 'blink']))


def nueva_lista():
    # Funcionalidad para agregar una lista numero por numero:
    print("Ingrese numeros de la lista uno por uno, para terminar ingrese un negativo: ")
    lista_nueva = []
    x = int(input())
    while (x >= 0):
        lista_nueva.append(x)
        x = int(input())
    buscar_numero(lista_nueva)


def usar_lista_hecha():
    # Funcionalidad para usar una lista ya creada:
    num = int(input("Ingrese el numero a buscar: "))
    cont = 0
    for i in range(len(list)):
        if list[i] == num:
            if i != 0 and list[i - 1] % 2 == 0 or i != (len(list) - 1) and list[i + 1] % 2 == 0:
                cont += 1
    print("El numero", num, "apareció", cont, "veces precedido o antecedido por un numero par")


def buscar_numero(lista_nueva):
    num = int(input("Ingrese el numero a buscar: "))
    cont = 0
    for i in range(len(lista_nueva)):
        if lista_nueva[i] == num:
            if i != 0 and list[i - 1] % 2 == 0 or i != (len(list) - 1) and list[i + 1] % 2 == 0:
                cont += 1
    return print("El numero", num, "apareció", cont, "veces precedido o antecedido por un numero par")


print_menu()
