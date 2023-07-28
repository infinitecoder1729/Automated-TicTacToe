<div align=center><h1>Automated TicTacToe</h1> </div>

<div align="center"><img src="https://github.com/infinitecoder1729/Automated-TicTacToe/assets/77016507/0ececa77-3c0c-4236-b85d-9042eedc10f7"></div>

A Program which allows user to play tic-tac-toe against the computer. The project was completed as a part of <a href="">CS50 AI course</a>. The Files runner.py (including but not limited to GUI implementation) and OpenSans-Regular.ttf was provided by the instructing team, however tictactoe.py which contains the logic which the computer uses has been implemented by me (@infinitecoder1729).

## To Run the program :
1. Download the program files at <a href="https://github.com/infinitecoder1729/Automated-TicTacToe/archive/refs/heads/main.zip">this link</a> and unzip or make a clone of the repo on local machine using ```git clone https://github.com/infinitecoder1729/Automated-TicTacToe.git```
2. Open the folder containing the files in terminal ```cd <The path of folder here>``` and run the ```python runner.py``` or ```python3 runner.py```

## Explanation of Logic implmented in tictactoe.py :

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L7-L9

These are constants used to represent players in the Tic Tac Toe game. X and O are used to identify the players, and EMPTY is used to indicate an empty cell on the game board.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L12-L18

The initial_state() function returns a 3x3 list representing the initial state of the Tic Tac Toe board, where all cells are empty.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L21-L43

The player(board) function determines which player has the next turn based on the current state of the board. It counts the number of Xs, Os, and empty cells on the board to make this decision. If X has played more moves than O, it's O's turn. If the board is empty, it's X's turn. Otherwise, if X and O have played the same number of moves, it's X's turn. If the board is full (no empty cells), the function returns None.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L46-L55

The actions(board) function returns a list of all possible moves (actions) that a player can make on the given board. It iterates over all cells of the board, and if a cell is empty (represented by EMPTY), it adds the cell coordinates (i, j) to the list of possible actions.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L58-L65

The result(board, action) function returns a new board that results from making a move (action) on the given board. It first determines the player making the move using the player() function, and then it creates a deep copy of the original board to avoid modifying it directly. It places the player's move at the specified action (i, j) on the new board and returns it.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L68-L84

The winner(board) function checks if there is a winner in the game. It does this by checking all rows, columns, and diagonals to see if they are occupied by the same player (X or O). If it finds a row, column, or diagonal where all cells have the same player's mark, it returns the mark of the player who won. If there is no winner, it returns None.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L87-L98

The terminal(board) function checks if the game is over. It returns True if there is a winner (by calling winner(board)) or if the board is completely filled (no empty cells). Otherwise, it returns False.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L101-L111

The utility(board) function determines the utility value of the terminal state (i.e., the final outcome of the game) for the maximizing player (X). If X wins, it returns 1, if O wins, it returns -1, and if it's a draw, it returns 0.

https://github.com/infinitecoder1729/Automated-TicTacToe/blob/6d467810f960e1d9bd4be0e278fb87c69f983a86/tictactoe.py#L113-L149

The minimax(board) function uses two helper functions, maximum(board) and minimum(board), to implement the minimax algorithm. The minimax algorithm is a recursive search algorithm used for decision-making in two-player zero-sum games, such as Tic Tac Toe.

The maximum(board) function calculates the maximum utility value for the maximizing player (X). If the board is in a terminal state (i.e., the game is over), it returns the utility value and an empty move. Otherwise, it initializes a threshold min_thresh to a very low value and iterates over all possible actions (moves) that X can make on the board. For each action, it calls the minimum() function with the resulting board and obtains the minimum utility value that the minimizing player (O) can achieve. It then updates min_thresh and the corresponding move if the minimum utility value is greater than the current min_thresh. Finally, it returns the min_thresh (maximum utility value) and the corresponding move that X should make to achieve that maximum utility.

The minimum(board) function calculates the minimum utility value for the minimizing player (O). If the board is in a terminal state, it returns the utility value and an empty move. Otherwise, it initializes a threshold max_thresh to a very high value and iterates over all possible actions (moves) that O can make on the board. For each action, it calls the maximum() function with the resulting board and obtains the maximum utility value that the maximizing player (X) can achieve. It then updates max_thresh and the corresponding move if the maximum utility value is smaller than the current max_thresh. Finally, it returns the max_thresh (minimum utility value) and the corresponding move that O should make to achieve that minimum utility.

In the minimax(board) function, the variable turn is used to determine whose turn it is (X or O). If the board is in a terminal state, it returns None since no further moves can be made. If it's O's turn, it calls the minimum() function to find the best move for O and returns that move. If it's X's turn, it calls the maximum() function to find the best move for X and returns that move.

This way, the minimax(board) function allows the AI player to choose the best possible move based on the minimax algorithm, ensuring that it maximizes its chances of winning or minimizing its chances of losing the game. It explores all possible moves and outcomes recursively to make an informed decision.

## Working :

https://github.com/infinitecoder1729/Automated-TicTacToe/assets/77016507/77edcc06-4c05-46ad-9a41-e80c35b76882

