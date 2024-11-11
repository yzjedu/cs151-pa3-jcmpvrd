# Programmers: Jordi
# Course:  CS151, Dr. Yalew
# Due Date: 11/7/2024
# Programming Assignment: 3
# Problem Statement: Creating a display of ASCII art and string decorations
# Data In: The design that the user wants to see
# Data Out: The design the user selected
# Credits: Class and ChatGPT for the third design

import random

def menu(): #Provides user with choices to choose from
    print("Choose an option:")
    print("1: Output a circle ")
    print("2: Output a set of lines")
    print("3: Output a random design")
    print("4: Exit")


def draw_circle(): #Draws a circle for the user
    print("    ***    ")
    print("  *     *  ")
    print(" *       * ")
    print(" *       * ")
    print("  *     *  ")
    print("    ***    ")


def draw_lines(): #Draws lines for the user
    try:
        lines_num = int(input("Enter the number of lines: "))
        lines_character = input("Please enter the characters you want to use for the design: ")
        repeat_count = int(input("How many times would you like to repeat this: "))
        print((lines_character * repeat_count + '\n') * lines_num)
    except ValueError:
        print("Invalid input. Please enter numeric values for the number of lines and repeat count.")


def design_one():  # This function creates a smiley face
    print("    ************    ")
    print("  *  _        _  *  ")
    print(" *  |_|      |_|   * ")
    print(" *       <        * ")
    print("  *  \\________/  *  ")
    print("    ************    ")


def design_two():  # This function creates a pyramid
    for i in range(1, 6):
        print(" " * (5 - i) + "*" * (2 * i - 1))


def design_three(): #This functions creates a heart and was used creating chat gpt
    print("        ******       ******")
    print("      **      **   **      **")
    print("    **         ** **         **")
    print("   **           ***           **")
    print("  **             *             **")
    print("  **                           **")
    print("   **                         **")
    print("    **                       **")
    print("      **                   **")
    print("        **               **")
    print("          **           **")
    print("            **       **")
    print("              **   **")
    print("                ***")
    print("                 *")


def random_design(): # Execute the randomly selected design function
    design_choice = random.choice([design_one, design_two, design_three])
    design_choice()


def main():
    choice = '0'
    while choice != '4':
        menu()
        choice = input("Please select something from the list (1-4): ")

        if choice == '1':
            draw_circle()
        elif choice == '2':
            draw_lines()
        elif choice == '3':
            random_design()
        elif choice == '4':
            print("Thanks for using the program.")
        else:
            print("Invalid choice. Please choose a number from 1-4.")


# Run the program
main()


