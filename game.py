import requests
import json

import api_calls
import auth
import board
import inputs
import bot

# module-level constants
BOT_TILE = 'O'
PLAYER_TILE = 'X'
OPEN_TILE = ' '
EMPTY_STR = ''
ACTIVE_STATUS = 'ACTIVE'
WINNER_STR = 'winner'
STATUS_STR = 'status'

# This module holds the guts of the program

# actual game mechanics
# ARGS: None
# RETURNS: None
def start_game() -> None:
    board_dict = {
        '7': OPEN_TILE, '8': OPEN_TILE, '9': OPEN_TILE,
        '4': OPEN_TILE, '5': OPEN_TILE, '6': OPEN_TILE,
        '1': OPEN_TILE, '2': OPEN_TILE, '3': OPEN_TILE
    }
    
    # setup new game and verify echo API responses return OK
    api_key, game_id = auth.set_up_and_auth_new_game()

    # new game status is NONE, but I'm gonna overwrite it to "Active"
    # Initialize winner, start game with X (player)
    status = ACTIVE_STATUS
    winner = EMPTY_STR
    current_tile_turn = PLAYER_TILE

    # print text, board before start of game
    inputs.print_game_start_text()
    board.print_board(board_dict)

    # use game status
    while status == ACTIVE_STATUS:
        # initialize
        current_move_tile = EMPTY_STR

        # get move from whoever's turn it is
        if current_tile_turn == PLAYER_TILE:
            current_move_tile = inputs.player_move()
        else:
            current_move_tile = bot.get_best_bot_move(board_dict)

        # sanitize user input and skip iteration ad hoc
        if (not inputs.is_user_input_valid_ints(current_move_tile) or
         not board.is_tile_valid(int(current_move_tile))):
            print("Try again with numbers 1-9 inclusive.")
            continue
        elif not board.is_tile_free(board_dict, current_move_tile):
            print("Tile has been taken. Please try again.")
            continue
        
        # successful user input, make API call for make_move
        board_dict[current_move_tile] = current_tile_turn
        x, y = board.get_x_y_from_tile(current_move_tile)
        make_move_response = api_calls.make_move(api_key, game_id, x, y, current_tile_turn).json()

        # update things after each successful move
        winner = make_move_response[WINNER_STR]
        status = make_move_response[STATUS_STR]
        
        # show board, update turn
        if current_tile_turn == BOT_TILE:
            print("Bot (O) has made a move to tile " + current_move_tile + ".")
        board.print_board(board_dict)
        current_tile_turn = update_turn(current_tile_turn)
        
    # end of game, print the winner, prompt game restart
    inputs.print_game_winner(status, winner)
    inputs.prompt_restart()

# update whose turn
# ARGS: current tile turn (str)
# RETURNS: 'X' or 'O' as strings
def update_turn(current_tile_turn: str) -> str:
    if current_tile_turn == PLAYER_TILE:
        return BOT_TILE
    return PLAYER_TILE

# this is the driver
if __name__ == "__main__":
    inputs.start_prompt()