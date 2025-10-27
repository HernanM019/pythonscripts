from termcolor import colored

def ask_to_continue():
    option = input("\nPresiona 1 para calcular otro valor. Cualquier otra tecla para volver al menú: ")
    return option == '1'

def get_number(prompt):
    while True:
        try:
            return int(input(colored(prompt, color='yellow')))
        except ValueError:
            print(colored("Entrada inválida. Por favor, ingresa un número válido.", color='red'))
