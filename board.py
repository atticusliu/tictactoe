import requests
import api_calls
import game

# This module holds all operations related to the board 

# board dictionary laid out like a numberpad:
# 7  8  9
# 4  5  6
# 1  2  3
# (0, 0) = 7, (0, 1) = 8, (0, 2) = 9
# (1, 0) = 4, (1, 1) = 5, (1, 2) = 6
# (2, 0) = 1, (2, 1) = 2, (2, 2) = 3

WINNING_COMBOS = [
    # across
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    # down
    ['7', '4', '1'],
    ['8', '5', '2'],
    ['9', '6', '3'],
    # diagonals
    ['7', '5', '3'], 
    ['9', '5', '1']
]

# takes either X or O and returns the winner
# ARGS: board (dict), whose turn (str)
# RETURNS: bool
def check_for_winner(board: dict, tile: str) -> bool:
    for combo in WINNING_COMBOS:
         if check_for_winner_subroutine(board, tile, combo):
             return True

    return False

# subroutine of check_for_winner that performs: A == B, B == C (therefore A == C) for a given tile
# ARGS: board (dict), tile (str), combo (one of the combos from WINNING_COMBOS)
# RETURNS: bool
def check_for_winner_subroutine(board: dict, tile: str, combo: list[str]) -> bool:
    spot0 = combo[0]
    spot1 = combo[1]
    spot2 = combo[2]

    if board[spot0] == board[spot1] and board[spot0] == board[spot2] and board[spot0] == tile:
        return True
    return False

# prints the board complete with what user input should look like
# ARGS: None
# RETURNS: None
def print_index_board() -> None:
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')

# prints current board
# ARGS: board (dict)
# RETURNS: None
def print_board(board: dict) -> None:
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# for a given tile, return the coordinates for use in api_calls
# ARGS: current tile (str)
# RETURNS: (x, y) as strings in a tuple
def get_x_y_from_tile(tile: str) -> tuple:
    index_x_y_dict = {
        '7': ('0', '0'),
        '8': ('0', '1'), 
        '9': ('0', '2'),
        '4': ('1', '0'),
        '5': ('1', '1'), 
        '6': ('1', '2'),
        '1': ('2', '0'),
        '2': ('2', '1'), 
        '3': ('2', '2'),
    }
    
    return index_x_y_dict[tile]

# quick method to return if a tile is free
# ARGS: board (dict)
# RETURNS: bool
def is_tile_free(board: dict, tile: str) -> bool:
    return board[tile] == game.OPEN_TILE

# quick method to return if user input as int is between 1-9 inclusive
# ARGS: tile (int)
# RETURNS: bool
def is_tile_valid(tile: int) -> bool:
    return tile >= 1 and tile <= 9