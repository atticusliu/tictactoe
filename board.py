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

# takes either X or O and returns the winner
# ARGS: board (dict), whose turn (str)
# RETURNS: bool
def check_for_winner(board: dict, tile: str) -> bool:
    if board['7'] == board['8'] and board['7'] == board['9'] and board['7'] == tile:
        return True
    elif board['4'] == board['5'] and board['4'] == board['6'] and board['4'] == tile:
        return True
    elif board['1'] == board['2'] and board['1'] == board['3'] and board['1'] == tile:
        return True
    elif board['7'] == board['4'] and board['7'] == board['1'] and board['7'] == tile:
        return True
    elif board['8'] == board['5'] and board['8'] == board['2'] and board['8'] == tile:
        return True
    elif board['9'] == board['6'] and board['9'] == board['3'] and board['9'] == tile:
        return True
    elif board['7'] == board['5'] and board['7'] == board['3'] and board['7'] == tile:
        return True
    elif board['1'] == board['5'] and board['1'] == board['9'] and board['1'] == tile:
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