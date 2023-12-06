# Math Quiz Project

   # 12/06/23

   # CTI-110 P5HW - Math Quiz

   # John Patrick Tejada

   #
   # Importing the necessary module for generating random numbers
import random

# Main function that runs the program
def main():
    print("Welcome to Math Quiz")
    
    while True:
        display_menu()  # Display the menu options to the user
        choice = input("Please choose one of the menu options: ")

        # Based on user's choice, call the respective function
        if choice == "1":
            add_random_numbers()
        elif choice == "2":
            subtract_random_numbers()
        elif choice == "3":
            print("Thank you for playing...\nBye!!")
            break
        else:
            print("Invalid choice. Please select from the given options.")

# Function to display the main menu
def display_menu():
    print("MAIN MENU")
    print("1. Add Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")

# Function to handle addition game
def add_random_numbers():
    num1 = random.randint(1, 100)  # Generate first random number
    num2 = random.randint(1, 100)  # Generate second random number
    correct_answer = num1 + num2   # Compute correct answer
    guess_count = 0                # Initialize the guess counter

    print(f"{num1: >3}\n+{num2: >2}\nEnter answer.")

    
    # Continuously prompt the user until they guess correctly
    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\ntry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\ntry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break

# Function to handle subtraction game
def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2
    guess_count = 0

    print(f"{num1: >3}\n-{num2: >2}\nEnter answer.")

    while True:
        guess = int(input())
        guess_count += 1
        if guess < correct_answer:
            print("Sorry, guess is too low.\ntry again: ", end="")
        elif guess > correct_answer:
            print("Sorry, guess is too high.\ntry again: ", end="")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {guess_count}")
            break

# Execute the main function if this script is run
if __name__ == "__main__":
    main()