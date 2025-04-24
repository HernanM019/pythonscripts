
#This is a modified version of the previous "time-calculator.py". This one was created using AI help to guide myself and
#understand the exception handling methods for Python.

#It also included several modifications in the script for make it easier to read and deleted repetitive calls.
#for instance, this version includes a specific function for it to be called each time we need to calculate another value
#after we just calculated a previous one. It introduced a methodology that I never used before such as "if not -> function" and
#break after.

from termcolor import colored


def ask_to_continue(): #New function, replaces old "while" loops in each function and instead calls this one each time
    option = input("\nPresiona 1 para calcular otro valor. Cualquier otra tecla para volver al menú: ")
    return option == '1'


def get_number(prompt):
    while True:
        try:
            return int(input(colored(prompt, color='yellow')))
        except ValueError:
            print(colored("Entrada inválida. Por favor, ingresa un número válido.", color='red'))


def weeks_to_months():
    while True:
        number = get_number('Ingresa una cantidad de semanas: ')
        months = number / 4.345  # promedio de semanas por mes
        print(f"{number} semanas son aproximadamente {months:.2f} meses.")
        if not ask_to_continue():
            break


def hours_to_seconds():
    while True:
        number = get_number('Ingresa una cantidad de horas: ')
        seconds = number * 3600
        print(f"{number} horas son {seconds} segundos.")
        if not ask_to_continue():
            break


def format_time():
    while True:
        number = get_number('Ingresa una cantidad de segundos: ')
        hours = number // 3600
        minutes = (number % 3600) // 60
        seconds = number % 60
        # new form of printing that i was exploring, although still not quite clear to me
        print(f"{number} segundos = {hours:02}:{minutes:02}:{seconds:02}")
        if not ask_to_continue():
            break


def seconds_to_hours():
    while True:
        number = get_number('Ingresa una cantidad de segundos: ')
        hours = number / 3600
        print(f"{number} segundos son {hours:.2f} horas.")
        if not ask_to_continue():
            break


def seconds_to_minutes():
    while True:
        number = get_number('Ingresa una cantidad de segundos: ')
        minutes = number / 60
        print(f"{number} segundos son {minutes:.2f} minutos.")
        if not ask_to_continue():
            break


def show_menu():
    print('\n' + colored('=== CALCULADORA DE TIEMPO ===', color='cyan', attrs=['bold']))
    print(colored('1) Semanas a meses', color='green'))
    print(colored('2) Horas a segundos', color='green'))
    print(colored('3) Segundos a HH:MM:SS', color='green'))
    print(colored('4) Segundos a horas', color='green'))
    print(colored('5) Segundos a minutos', color='green'))
    print(colored('9) Salir del programa', color='yellow'))


def main():
    print(colored('ver 2.0', color='blue'))
    print(colored('\nBienvenido a tu calculadora de tiempo\n', color='cyan'))

    while True:
        show_menu()
        try:
            opt = int(input(colored("Selecciona una opción: ", color='red')))
        except ValueError:
            print(colored("Opción inválida. Recuerde que tiene que escoger con numeros. Intente nuevamente.\n", color='red'))
            continue

        if opt == 1:
            weeks_to_months()
        elif opt == 2:
            hours_to_seconds()
        elif opt == 3:
            format_time()
        elif opt == 4:
            seconds_to_hours()
        elif opt == 5:
            seconds_to_minutes()
        elif opt == 9:
            print(colored("¡Hasta la próxima!", color='cyan'))
            break
        else:
            print(colored("Opción inválida. Por favor, selecciona un número del menú.", color='red'))


if __name__ == '__main__':
    main()
