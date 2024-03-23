<h1>Tic-Tac-Toe Game using Minimax Algorithm</h1>
This Python script implements the classic Tic-Tac-Toe game where the player competes against the computer. The computer's moves are determined using the Minimax algorithm, a recursive algorithm used in decision-making and game theory.

**Overview**  
The game is played on a 3x3 grid where players take turns marking spaces with their respective symbols ('X' for the computer and 'O' for the human player). The game continues until one player wins by getting three of their symbols in a row, column, or diagonal, or if the game ends in a draw.

**Features**  
`Human vs. Computer:` Play against an intelligent computer opponent.
`Minimax Algorithm:` The computer's moves are determined using the Minimax algorithm, ensuring optimal play.
`Simple Interface:` The game interface is user-friendly and interactive.  

**How to Play**  
* Run the script using Python `(python tictactoe_minimax.py)`.
* Input moves using the numpad keys (1-9) to place your symbol ('O') on the board.
* The computer ('X') will automatically make its moves using the Minimax algorithm.
* Continue playing until the game ends.
* The game will display the outcome (win, lose, or draw) at the end.
  
**Implementation Details**  

`evaluate(state):` Evaluates the current state of the board to determine the game's outcome.  
`wins(state, player):` Checks if the given player has won the game based on the current board state.  
`game_over(state):` Checks if the game is over (either a player has won or the board is full).  
`empty_cells(state):` Returns a list of empty cells on the board.  
`valid_move(cell):` Checks if a given cell is a valid move (i.e., empty).  
`set_move(cell, player):` Marks the specified cell with the player's symbol.  
`minimax(state, depth, player):` Implements the Minimax algorithm to determine the best move for the computer.  
`render(state, c_choice, h_choice):` Renders the current state of the board.  
`ai_turn(c_choice, h_choice):` Handles the computer's turn.  
`human_turn(c_choice, h_choice):` Handles the human player's turn.  
`main():` Main function to start the game.  
