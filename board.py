import requests
import api_calls

# This file holds all operations related to the board 


# board dictionary laid out like a numberpad:
# 7  8  9
# 4  5  6
# 1  2  3
# (0, 0) = 7, (0, 1) = 8, (0, 2) = 9
# (1, 0) = 4, (1, 1) = 5, (1, 2) = 6
# (2, 0) = 1, (2, 1) = 2, (2, 2) = 3

def print_index_board() -> None:
    print('7' + '|' + '8' + '|' + '9')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('1' + '|' + '2' + '|' + '3')

def print_board(board: dict) -> None:
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# is there a better way to do this lmao
# RETURNS: (x, y) as strings in a tuple
def get_x_y_from_spot(spot: str) -> tuple:
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
    
    return index_x_y_dict[spot]

# RETURNS bool. returns if input is between 1-9 inclusive
def is_spot_valid(tile_spot: int) -> bool:
    return tile_spot >= 1 and tile_spot <= 9
