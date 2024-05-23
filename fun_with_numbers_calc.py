"""Fun With Numbers by Ashwin Tenneti"""
#import function imports libraries into the program
from operator import add
from operator import sub
from operator import mul
from operator import truediv
import os
import fontstyle

#sets these variables to 0.
NUMBER_COUNT = 0
NUMBER_TOTAL = 0
SMALLEST_NUMBER = 0
LARGEST_NUMBER = 0
PLOT_COUNT = 0

#def main defines the main function.
def main():
    """Landing page and main user interface for the app"""
    load_stats()
    exit_flag = False
    #sets the exit condition as false

    #main function will continue to loop, whilst exit_flag == false
    while not exit_flag:
        clear_console()
        print(fontstyle.apply("Welcome to Fun with Numbers!", 'GREEN/UNDERLINE'))
        print("\n Choose from the menu below:")
        print(" (A) Check number features")
        print(" (B) Plot numbers")
        print(" (C) Check overall stats")
        print(" (D) Calculator")
        print(" (E) Creator and Background")
        print(" (H) How to Use")
        print("\n (X) save and exit")
        choice = input("\nchoice: ").upper()

            #opens and runs sub-routines based on user inputs
        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            stats()
        elif choice == "D":
            calculator()
        elif choice == "E":
            creator()
        elif choice == "H":
            how_to_use()
        elif choice == "X":
            save_stats()
            print(fontstyle.apply("\n Fun With Numbers successfully closed. Data saved on stats.txt. Have a nice day! \n", 'YELLOW'))
                #updates exit_flag to true and closes the software.
            exit_flag = True
        else: print(fontstyle.apply("Invalid input, please try again", 'RED'))

def number_features():
    """displays features of the chosen number"""
    clear_console()

    global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER
    print(fontstyle.apply("Number features \n", 'BLUE/BOLD/UNDERLINE'))
    number = int(input("Please enter a whole number to be checked: "))
    clear_console()
    print(f"The features of {number} are...")

    #determines if number is positive or negative
    if number > 0:
        print("\n positive")
    #elif stands for else if. Runs when if doesn't work
    elif number < 0:
        print("\n negative")
    else:
        print("\n zero")

    #determines if number is an odd number or an even number
    if number % 2 == 0:
        print(" Even")
    else:
        print(" Odd")

    #Lists the factors of number
    factor_count = 0
    print(" Factors are", end="")
    if number > 0:
        for i in range(1, number + 1):
            if number % i == 0:
                print(" " + str(i), end="")
                factor_count += 1
    if number < 0:
        for i in range(number - 1, -1):
            if number % i == 0:
                print(" " + str(i), end="")
                factor_count += 1
    #indicates if number is prime or not
    if factor_count == 2:
        print("\n Is prime number")
    else:
        print("\n Is not a prime number")

    input("\n Press enter to continue...")

    #updates the global variable
    if NUMBER_COUNT == 0:
        SMALLEST_NUMBER = number
        LARGEST_NUMBER = number
    else:
        SMALLEST_NUMBER = min(number, SMALLEST_NUMBER)
        LARGEST_NUMBER = max(number, LARGEST_NUMBER)

    NUMBER_COUNT += 1
    NUMBER_TOTAL += number

def plotter():
    """Plots the number on a graph"""
    clear_console()
    print(fontstyle.apply("Number Plotter: ", 'BLACK/BOLD/UNDERLINE'))
    global PLOT_COUNT
    #shows how many column spces and row spaces we have
    num_columns = 38
    num_rows = 12
    table = [[" " for column in range (num_columns)]for row in range(num_rows)]

    while True:
        try:
            #ask user for a set of coordinates (x and y coordinates. one for each axis)
            x_axis = int(input("\n Enter x axis (1-38): "))
            y_axis = int(input("\n Enter y axis (1-12): "))

            #tests if the values entered are valid
            if 1 <= x_axis <= 38 and 1 <= y_axis <= 12:
                table[y_axis - 1][x_axis -1] = "💩"

                #updates the plot_count global variable
                PLOT_COUNT += 1

                print_table(table)
                another_plot = input(" Do you wish to plot another coordinate (y/n)?").lower()
                if another_plot != "y":
                    break
            else:
                print(fontstyle.apply("Invalid coordinates, please enter valid numerals", 'RED'))
        except ValueError:
            print(fontstyle.apply("Invalid input. Please enter integers for coordinates", 'RED'))

#defines the print_table function
def print_table(table):
    """Prints the table for the plotter sub-routine function"""
    print("\n                                                       x axis")
    print("    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ")
    print("    -----------------------------------------------------------------------------------------------------------------")
    #takes gthe content of tbale and pints into the plotter graph.
    for index, row in enumerate(table, start = 1):
        print(f"{index:2}| {'  '.join(row)}| ")
    print("    -----------------------------------------------------------------------------------------------------------------")

def stats():
    """Displays statistics of numbers used in the program"""
    clear_console()
    print(fontstyle.apply("Here is the statistics of overall use:", 'PURPLE/UNDERLINE'))
    print(f"\n Numbers entered: {NUMBER_COUNT}")
    print(f" Total of numbers: {NUMBER_TOTAL}")
    print(f" Average of numbers: {NUMBER_TOTAL/NUMBER_COUNT}")
    print(f" smallest number entered: {SMALLEST_NUMBER}")
    print(f" Largest number entered: {LARGEST_NUMBER}")
    print(f" Coordinates plotted: {PLOT_COUNT}")
    input("\nPress Enter to continue...")

def clear_console():
    """Clears the console between routines"""
    #runs clear_console depeing on the users operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def save_stats():
    """Saves statistics from current session into file"""
    #utf is the unverisal standard used by all systems. the encoding=utf-8 is kind of just saying that we use this font to print.
    with open("stats.txt", "w", encoding="utf-8") as file:
        file.write(f"{NUMBER_COUNT}\n")
        file.write(f"{NUMBER_TOTAL}\n")
        file.write(f"{SMALLEST_NUMBER}\n")
        file.write(f"{LARGEST_NUMBER}\n")
        file.write(f"{PLOT_COUNT}\n")

def calculator():
    """Simple Calculator"""
    clear_console()
    print(fontstyle.apply("Select an Option...", 'CYAN/UNDERLINE/BOLD'))
    print("\n 1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")

    while True:

        choice_1 = input("\n Enter required Option...")

        if choice_1 in ('1', '2', '3', '4'):
            try:
                #makes values as floats/numbers when it asks for an input.
                num1 = float(input("Enter First Number..."))
                num2 = float(input("Enter Second Number..."))
            except ValueError:
                print(fontstyle.apply("Invalid input. Please enter appropriate values.", 'RED'))
                continue

            if choice_1 == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice_1 == '2':
                print(num1, "-", num2, "=", sub(num1, num2))

            elif choice_1 == '3':
                print(num1, "x", num2, "=", mul(num1, num2))

            elif choice_1 == '4':
                print(num1, "÷", num2, "=", truediv(num1, num2))

            else:
                input(fontstyle.apply("Invalid inputs. Please press enter to continue...", 'RED'))

            continue_calculations = input("Another Calculation? y/n")
            if continue_calculations == 'n':
                break
            else:
                print(fontstyle.apply("Invalid Input.", 'RED'))

def how_to_use():
    """Help page for users"""
    clear_console()
    print(fontstyle.apply("Welcome to fun with Numbers!", 'YELLOW/UNDERLINE/BOLD'))
    print("\nThis programme is a very basic software that as the name suggests, has a few features for finding the features of numbers.")
    print("It includes a number feature, a plotter feature and calculator feature.")
    print("\nHow use. Use the alphabets on the screen to access the different options.")
    print("Be sure to save and exit once you are done using it. Have Fun!")
    input("\nPress enter to return to main menu...")

def creator():
    """Creator and background page."""
    clear_console()
    print(fontstyle.apply("\n Welcome to fun with Numbers! - (Ashwin Edition)", 'PURPLE/UNDERLINE/BOLD'))
    print("\n Fun with numbers is a very useful tool that you can use in your daily life!")
    print("The creator Ashwin Tenneti has dedicated countless amounts of research to make this programme the most accesible by anyone")
    print("Enjoy Fun with Numbers! Please be sure to tell all you friends about his programme!")
    print("\n Creator...")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("****************************************//(((((####%%%#########((((((/********************")
    print("********************************//((#%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%#(//***********")
    print("***************************/(#%&&&&&&&&&&&&&&&&@&&&&&&&&&&&&&&@@@@@@@@@@@@@@@&&%#/********")
    print("***********************/(%&&&&&&@&@@@@@@&@@@@&&&&&%%&%&&&&&&&&&&@@@@@@@@@@@@@@@@@&#/******")
    print("********************/(#%&&&&&&&&&&@@@@@@&&&&&&&%%%&&&&&&%&&&&@@&&&&&%&&&&&&@@@@@@&&#/***,,")
    print("******************/#%&&&&&&&&&&&@@@@&&@&&&&&&&&&&@&&@@@@@&&&@@@@&&&&&&&&&%&&@&&&&&&&(/**,*")
    print("*****************(%&&&&&&&&&&&&&&&&&&&&&&&&&&@@@@@@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&#/****")
    print("***************/#&&&&&&&&@@@@@@&&&&&&&@@@@@&&&&&&@@@@@@@&&@@@@@@@@@@@@@@@&&&@@@@@@&%/**,**")
    print("**************/%&&&&&&&@@@@@@@&&&&&&&&&&&&&&&&&&&%%%%%%####%%%%%&&&&@@@@@@@@@@@@@&#/***,**")
    print("*************/#&&&&&&&@@@@@@@&&&&&&&&%%%%%%%######((((((((((#####%%%&&&@@@@@@@@@&(****,,**")
    print("*************(%&&&@@&&@@@@@@@@&&&%%#(((((((((((((/////////(((((###%%%%%&&@@@@@@@&#/*,,,,,*")
    print("************(%&&&@@@&&@@@&&&&&%#(((((///////////*//////////////(((##%%%%&&&&@@@@@@%/*,,,,,")
    print("************#&&&&&&&&&&&&%&&%##((((/////******************///////(((###%%%%&&&@@@@&#**,,,,")
    print("************#&&&&&&@@@&&&%%##((((((/////*********************////((((###%%%%%&&@@@@&(*,,,,")
    print("*********,**#&&&&&&&&&&%%####((((((////**********************////((((######%%%&&&@@&#/,,,,")
    print(",,,*****,,**#&&&&&&&&&%%#####(((((/////********,,*************////((((#####%%%&&&&&&%/*,,,")
    print(",,,,,*******#&&&&&@@&%%#######((((///********,,****,************///((((####%%%%&&&&&%/*,,,")
    print(",***********(%&&@@&&%######%%%%%%#####(((///**************////((####%%%%%%%%%%%%&&@&#/*,,,")
    print(",***********(%&@@&%%###%%%%##(((((((#####((((/////*****///((((#######(((##%%%%%%%&@&#/*,,,")
    print(",*,,,,,,,***(%@@@&%%##%%#(((/////////(((((((((///////////((((###((((((////(##%%%%&&&(/,,,,")
    print(",,,,,,,,,,,*/%&@@&%#####((((##(((((((((((((((((//****//(((###((((///((((((((##%%%&&&/*,,,,")
    print(",*,,,,,,,,,*/#&@&&%###((((#%%%##%&&&&#//((((((((/////((((((((((##%%%%%%%#########%&%/*,,,,")
    print(",,,,,,,,,,,**#&&&&%##(((((####((/(##(//////(((((((//(((((((((**/#&&%(/(#%%%######%%(*,,,,,")
    print(",*******(###(#&&&%%##(((////((((((/////////(((((((//((((((((///(((((((######((###%%#//****")
    print("******/(####((#%&&%##(((//////////***//////((((((/////(((((((//**///((((((((((###%%%#%%#/*")
    print("******/(#((((((#%%%###(((////////////***//((((((///////((##(((////*////////(((###%%####(/*")
    print("******/(((##(###%%%%###((///*************/(((((//*****//((##((/////////////(((###%####(/**")
    print("*******/(#((((####%%###(((//*****,,,****/((//////**,***///((((/******//////((########(/*,*")
    print("********((((((((###%####((///**********/(((/(###(/////((((//(((/*******///(((######((/****")
    print("********/(((##((((#######((////******////((((((///((((((#####((//******///((#######((/****")
    print("*********((###############((((//((//////////////*****///(///((((/////////((##########(/***")
    print("*********/(((((((#(########(((((((((###((((((///////////((((((((((((((((((###########(/***")
    print("***********/(((((((((######((((((##%%%######((((((///((((((((#######(((((###########(/****")
    print("*********************(###((((((((//((##%%%####((((((((((#####%%%&%%###((######((((((******")
    print("*********************/###(((((((((///(((((((((///****///((##%%##((((((((####(/************")
    print("**********************(####((((((((((((((((((((((((////(((####(((((((((####(/*************")
    print("**********************(######((((((((((//////((((((((((#(((((((((((((#####(/**************")
    print("**********,,,*********/########((((((((////////////////////((((((((#####(/****************")
    print("********,,,***********/(###########((((((((////**/////////((((((########(*****************")
    print("**********************/(#############((((((/////////////((((((########%#/*******,*********")
    print("***********************(###############((((((((((((((((((((((########%%(/*****************")
    print("***********************(##########################((((###############%%(/*****************")
    print("***********************(###((((#######################################%(/*****************")
    print("***********************(##(((((((#######################################/*****************")
    print("***********************(##(((((/(((((#(((((((((((((###############(#####(*****************")
    print("**********************/(##(((///////(((((((//////////(((((####(((((((###(*****************")
    print("***************,,*(#(((###(((////////((((((///////////((((###(((((((((####(/**************")
    print("*************,,.,(%%######(((//////////(((((((//////(((((((#(((///((((###%%#/,,***********")
    print("*************,. ,/%%%####((((///////////((((/////(/(((((((((((////((((####%%(..,**********")
    print(",*******,,,,,... ,(#####(((((/////////////(//////////(((((((//////(((((###%(,..,,,,,,*****")
    print(",***,,..........  ./##((((((///////////////////////////((((////////(((((##/,............,*")
    print(",,...        ....   ,/((((((///////////////////////////////////////(((((/,......     .   .")
    print("......                ,*/(//////////////////////////////////////////((/,. ....            ")
    print("........                .**/////////////////////////////////////////*,                    ")
    print("....  ...                .,***************/////////////////////*,.                      ")
    print("....      .                  ..,,,,,,**********/*************,..                        ")
    print("....    ..                ...       .*/****************/*,.                            ")
    input("\n Press enter to continue and experience the world of Fun with Ashwin...")

def load_stats():
    """Loads statistics from previous sessions"""
    #os is a library. calling path.exits from the os libaray.
    if not os.path.exists("stats.txt"):
        return
    with open("stats.txt", "r", encoding="utf-8") as file:
        global NUMBER_COUNT, NUMBER_TOTAL, SMALLEST_NUMBER, LARGEST_NUMBER, PLOT_COUNT
        NUMBER_COUNT = int(file.readline())
        NUMBER_TOTAL = int(file.readline())
        SMALLEST_NUMBER = int(file.readline())
        LARGEST_NUMBER = int(file.readline())
        PLOT_COUNT = int(file.readline())

    #"w" function means write. We are storing information in the variable. utf-8 is the most unviersal coding system.

#calls the main function
main()
