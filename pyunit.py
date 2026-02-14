import random

# Holds the game choices
CHOICES = ["rock", "paper", "scissors"]

# Maps the different win scenarios.
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


# Function that determines if the user or program won the game.
def calculate_winner(user, program):

    # Executes if the user and program chose the same option
    if user == program:
        return "tie"
    
    # Executes if the user chose an option that beats the program's option.
    if BEATS[user] == program:
        return "user"
    
    # Executes if the above if statements weren't true, meaning that the program had the winning choice.
    return "program"


# Function that sets up the majority of dialogue along with determining user + program input.
def game():

    #Welcome Message
    print("\nWelcome to Rock, Paper, Scissors!") 

    # The continuation of the game is placed in a while loop.
    while True:

        # Asks for user input and stores it
        user_choice = input("Rock, Paper, or Scissors? (q to quit)\n").lower() 
        
        # Ends the game.
        if user_choice == "q": 
            break
        
        # Loops the user until they respond with a valid option.
        while user_choice not in CHOICES: 
            print("You response was:", user_choice)
            user_choice = input("This is not a valid choice. Either choose rock, paper, or scissors!\n").lower()

        #The program picks a random choice.
        program_choice = random.choice(CHOICES) 

        # Call to the function calculate_winner and stores the return value into winner.
        winner = calculate_winner(user_choice, program_choice) 

        # Print statement post game calculation
        print("\nYou chose", user_choice, "\nThe program chose", program_choice) 

        # Victory message
        if winner == "user":
            print("\nYou won!\n")
        elif winner == "program":
            print("\nThe program won!\n")
        else:
            print("\nYou and the program tied!\n")
        

if __name__ == "__main__":
    game()