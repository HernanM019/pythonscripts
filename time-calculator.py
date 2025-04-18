import sys

from termcolor import colored


def main():
    opt = 0
    print('ver0.1')
    print('\nWelcome to your time calculator: \n'),
    while opt != 9:
        print('Please SELECT AN OPTION: \n')
        print(colored('1) Calculate weeks to months', color='green'))
        print(colored('2) Calculate hours to seconds', color='green'))
        print(colored('3) Calculate seconds to HH-MM-SS', color='green'))
        print(colored('4) Calculate seconds to hours', color='green'))
        print(colored('9) EXIT PROGRAM', color='yellow'))
        opt = int(input(colored("Your option: ", color='red')))
        if opt == 1:
            weeks_to_months()
        elif opt == 2: #TODO
            print(colored("This option was NOT developed yet. Please come back later", color='cyan'))

        elif opt == 3:
            hours_to_format()
        elif opt == 4: #TODO
            print(colored("This option was NOT developed yet. Please come back later", color='cyan'))

        elif opt == 9:
            sys.exit()
        else:
            print(colored("ERROR!! Invalid option, please retry", color='red', attrs=['bold', 'blink']))


def hours_to_format():
    while True:
        number = int(input(colored('Please insert a number: ', color='yellow')))

        def convert(seconds):
            seconds = seconds % (24 * 3600)
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            x = "%d:%02d:%02d" % (hour, minutes, seconds)
            return x

        print("Your result is: ", convert(number))
        option = int(input("\nInput ANY VALUE to go back to the previous menu \n"
                  "Press 1 to calculate another value: "))
        if option != 1:
            break

def weeks_to_months():
    while True:
        number = int(input(colored('Please insert a number of weeks: ', color='yellow')))

        def convert(weeks):
            months = weeks / 4.345
            return months

        print("Your result is: ", convert(number))
        option = int(input("\nInput ANY value to got back to the previous menu \n"
                      "Press 1 to calculate another value: "))
        if option != 1:
            break



if __name__ == '__main__':
    main()

