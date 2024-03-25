##     Snake-Water-Gun-Game-in-Python in with Tkinter GUI

This Python program implements a classic Rock, Paper, Scissors (Snake, Water, Gun) game with a user-friendly graphical interface using the Tkinter library.

**Features:**

- Play against the computer.
- Choose from Snake, Water, or Gun.
- Get visual feedback on win, lose, or draw outcomes.

**Requirements:**

- Python 3.x with Tkinter library installed (usually comes pre-installed)

**Instructions:**

1. Save the code as a Python file (e.g., `rock_paper_scissors.py`).
2. Open a terminal or command prompt and navigate to the directory where you saved the file.
3. Run the script using `python rock_paper_scissors.py`.
4. Select your choice (Snake, Water, or Gun) from the dropdown menu.
5. Click the "Play" button to start a round.
6. The result (win, lose, or draw) will be displayed on the screen.

**Gameplay:**

- Snake defeats Water (Water gets drunk by Snake).
- Water defeats Gun (Gun gets rusted by Water).
- Gun defeats Snake (Gun shoots Snake).
- Choosing the same option results in a draw.

**Code Structure:**

The code consists of several functions:

- `play_game()`: Generates computer's choice, maps user input, checks results, and updates the display.
- `check(value, user)`: Determines win, lose, or draw based on the computer's and user's choices.
- `update_result_text(score)`: Sets the result text (win, lose, or draw) based on the score.

**Additional Notes:**

- You can customize the window title and button text if desired.
- Feel free to experiment with different GUI layouts using Tkinter's widgets.

**Enjoy playing!**
