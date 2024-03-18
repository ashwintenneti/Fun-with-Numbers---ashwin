"""Fun With Numbers by Ashwin Tenneti"""
import os

def main():
    """Landing and main user interface for the app"""
    exit_flag = False
    while not exit_flag:
        clear_console()
        print("Welcome to Fun with Numbers")
        print("Choose from the menu below:")
        print(" (A) Check number features")
        print(" (B) Plot numbers")
        print(" (C) Check overall stats")
        print("\n (X) save and exit")
        choice = input("\nchoice:").upper()

        if choice == "A":
            number_features()
        elif choice == "B":
            plotter()
        elif choice == "C":
            stats()
        elif choice == "X":
            exit_flag = True
        else: print("Invalid input, please try again")
def number_features():
    """displays featueres of the chosen number"""
    clear_console()
    print("this is the number features of the sub routine")
    input("\nPress Enter to continue...")

def plotter():
    """Plots the number on a graph"""
    clear_console()
    print("this is a plotter sub-routine")
    input("\nPress Enter to continue...")

def stats():
    """Displays statisitics of numbers used in the program"""
    clear_console()
    print("this is the stats sub-routine")
    input("\nPress Enter to continue...")

def clear_console():
    """Clears the console between routines"""
    os.system('cls' if os.name == 'nt' else 'clear')
    input("\nPress Enter to continue...")

main()
