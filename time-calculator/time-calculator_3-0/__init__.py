
#Here's the initialization python script for creating a modular version for the time-calculator script developed in versions 1 and 2

#This init file is useful for importing files from one module to another without encountering issues. It's not enforced since python 3.3
#However it is still quite useful for picking specific functions from different modules to be imported in specific scripts or other modules.

#Here's the structure this modular script will have:

#time_calculator/
#│
#├── __init__.py
#├── main.py            # Main menu and main interaction loop
#├── utils.py           # All functions that would allow the program to basically operate between modules
#                       # such as get_number(), ask_to_continue()
#└── converters.py      # All main functions from the main menu. The main program basically. weeks_to_months(), format_time(), etc.