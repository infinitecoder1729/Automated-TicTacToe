"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX=0
    countO=0
    countEmpty=0
    for i in board:
        for j in i:
            if j==X:
                countX+=1
            elif j==O:
                countO+=1
            else :
                countEmpty+=1
    if countX>countO:
        return O
    elif countEmpty==9:
        return X
    elif countX==countO:
        return X
    else :
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act=[]
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]==EMPTY:
                act.append((i,j))
    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    move=player(board)
    new_board=deepcopy(board)
    new_board[action[0]][action[1]]=move
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for mark in (X, O):
            for row in board:
                if row == [mark] * 3:
                    return mark
            for i in range(3):
                column = [board[x][i] for x in range(3)]
                if column == [mark] * 3:
                    return mark
            if [board[i][i] for i in range(0, 3)] == [mark] * 3:
                return mark
            elif [board[i][~i] for i in range(0, 3)] == [mark] * 3:
                return mark                
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    
    for i in board:
        for j in i:
            if j==EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    playerwin = winner(board)
    if playerwin == X:
        return 1
    elif playerwin == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maximum(board):
        move=()
        if terminal(board):
            return utility(board),move
        else:
            min_thresh=-100
            for act in actions(board):
                mini=(minimum(result(board,act))[0])
                if mini>min_thresh:
                    min_thresh=mini
                    move=act
            return min_thresh,move
    def minimum(board):
        move=()
        if terminal(board):
            return utility(board),move
        else:
            max_thresh=100
            for act in actions(board):
                maxi=(maximum(result(board,act))[0])
                if maxi<max_thresh:
                    max_thresh=maxi
                    move=act
            return max_thresh,move
    turn=player(board)
    if terminal(board):
        return None
    if turn==O:
        return minimum(board)[1]
    elif turn==X:
        return maximum(board)[1]
    return None
