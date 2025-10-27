from termcolor import colored
from converters import weeks_to_months, format_time, seconds_to_hours, seconds_to_minutes, hours_to_seconds

def show_menu():
    print('\n' + colored('=== CALCULADORA DE TIEMPO ===', color='cyan', attrs=['bold']))
    print(colored('1) Semanas a meses', color='green'))
    print(colored('2) Horas a segundos', color='green'))
    print(colored('3) Segundos a HH:MM:SS', color='green'))
    print(colored('4) Segundos a horas', color='green'))
    print(colored('5) Segundos a minutos', color='green'))
    print(colored('9) Salir del programa', color='yellow'))

def main():
    print(colored('ver 3.0', color='blue'))
    print(colored('\nBienvenido a tu calculadora de tiempo (modularizada)\n', color='cyan'))

    while True:
        show_menu()
        try:
            opt = int(input(colored("Selecciona una opción: ", color='red')))
        except ValueError:
            print(colored("Opción inválida. Intente nuevamente.\n", color='red'))
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
            print(colored("Muchas gracias. Programa cerrado", color='cyan'))
            break
        else:
            print(colored("Opción inválida. Por favor, selecciona un número del menú.", color='red'))


if __name__ == '__main__':
    main()
