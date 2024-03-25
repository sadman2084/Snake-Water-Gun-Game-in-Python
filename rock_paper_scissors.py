from tkinter import *
import random

def play_game():
    value = random.randint(0, 2)  # Generate computer's choice (0: Snake, 1: Water, 2: Gun)

    # Map user input to choice values
    user_choice = {
        "Snake": 0,
        "Water": 1,
        "Gun": 2
    }[user_choice_var.get()]

    score = check(value, user_choice)

    update_result_text(score)

def check(value, user):
    # Winning conditions
    if (value + 1) % 3 == user:
        return 1  # Win
    elif value == user:
        return 0  # Draw
    else:
        return -1  # Lose

def update_result_text(score):
    if score == 0:
        result_text.set("It's a draw!")
    elif score == 1:
        result_text.set("You win!")
    else:
        result_text.set("You lose!")

# Create the main window
window = Tk()
window.title("Rock, Paper, Scissors (Snake, Water, Gun)")

# Text label for user input
user_choice_label = Label(window, text="Your Choice:")
user_choice_label.pack()

# User choice selection (dropdown)
user_choice_var = StringVar(window)
user_choice_var.set("Snake")  # Default selection
user_choice_menu = OptionMenu(window, user_choice_var, "Snake", "Water", "Gun")
user_choice_menu.pack()

# Play button
play_button = Button(window, text="Play", command=play_game)
play_button.pack()

# Result text variable
result_text = StringVar()

# Result label
result_label = Label(window, textvariable=result_text)
result_label.pack()

# Start the main event loop
window.mainloop()
