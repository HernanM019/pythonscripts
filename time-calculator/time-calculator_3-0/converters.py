from termcolor import colored
from .utils import get_number, ask_to_continue

def weeks_to_months():
    while True:
        number = get_number('Ingresa una cantidad de semanas: ')
        months = number / 4.345
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