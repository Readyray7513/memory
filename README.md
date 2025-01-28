# History Tracker Program
This Python program tracks a series of actions entered by the user. The user can add actions to the history, undo the most recent action, restart the history, or stop the program.

Requirements:
Python 3.x

How to Use:
Run the script.
Enter actions as text. Each action will be added to the history.

Use the following commands:
Undo: Undoes the most recent action and removes it from the history.
Restart: Clears the entire history.
End: Exits the program.

The program will display the current history after each action is taken.
Example:
Input/Output:
Action: Action1
['Action1']
Action: Action2
['Action1', 'Action2']
Action: Undo
Undone: Action2
['Action1']
Action: Restart
Action: End

Explanation of the Code:
History is stored in a list called history.
The program enters a loop where it waits for user input.
If the input is Undo, the most recent action is removed using the pop() function, and the undone action is printed.
If the input is Restart, the entire history is cleared using the clear() function.
Any other input is added to the history using the append() method.
When End is entered, the loop breaks, and the program stops.

How It Works:
The user inputs actions.
The program responds based on the action entered:
Adds actions to history.
Undoes actions with the Undo command.
Clears history with the Restart command.
Exits with the End command.
