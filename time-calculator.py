from termcolor import colored
import sys


def main():
    opt = 0
    print('ver0.1')
    print('\nWelcome to your time calculator: \n'),
    while opt != 9:
        print('Please SELECT AN OPTION: \n')
        print(colored('1) Calculate weeks to months', 'green'))
        print(colored('2) Calculate hours to seconds', 'green'))
        print(colored('3) Calculate seconds to HH-MM-SS', 'green'))
        print(colored('4) Calculate seconds to hours', 'green'))
        print(colored('9) EXIT PROGRAM', 'yellow'))
        opt = int(input(colored("Your option: ", 'red')))
        if opt == 1:
            print(colored("This option was NOT developed yet. Please come back later", 'cyan'))
            pass
        elif opt == 2:
            print(colored("This option was NOT developed yet. Please come back later", 'cyan'))
            pass
        elif opt == 3:
            hours_to_format()
        elif opt == 4:
            pass
        elif opt == 9:
            sys.exit()
        else:
            print(colored("ERROR!! Invalid option, please retry", 'red', attrs=['bold', 'blink']))


def hours_to_format():
    number = int(input(colored('Please insert a number: ', 'yellow')))

    def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        x = "%d:%02d:%02d" % (hour, minutes, seconds)
        return x

    print("Your result is: ", convert(number))
    x = int(input("\nInput ANY VALUE to go back to the previous menu \n"
                  "Press 1) to calculate another value: "))
    if x == 1:
        hours_to_format()
    else:
        pass


if __name__ == '__main__':
    main()

