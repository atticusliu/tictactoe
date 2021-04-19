import requests
import json
# I got a feeling these imports are NOT preferable
import api_calls
import auth
import board
import inputs
import bot

# globals
bot_tile = 'O'
player_tile = 'X'
open_tile = ' '
empty_str = ''
active_status = 'ACTIVE'
winner_str = 'winner'
status_str = 'status'

# This file holds the guts of the program

# actual game mechanics
def start_game() -> None:
    board_dict = {
        '7': open_tile, '8': open_tile, '9': open_tile,
        '4': open_tile, '5': open_tile, '6': open_tile,
        '1': open_tile, '2': open_tile, '3': open_tile
    }
    
    # setup new game and verify echo API responses return OK
    api_key, game_id = auth.set_up_and_auth_new_game()

    # new game status is NONE, but I'm gonna overwrite it to "Active". Initialize winner, start game with X (player)
    status = active_status
    winner = empty_str
    current_tile_turn = player_tile

    # print text, board before start of game
    inputs.print_game_start_text()
    board.print_board(board_dict)

    # use game status
    while status == active_status:
        # initialize
        current_move_tile = empty_str

        # get move from whoever's turn it is
        if current_tile_turn == player_tile:
            current_move_tile = inputs.player_move()
        else:
            current_move_tile = bot.get_best_bot_move(board_dict)

        # sanitize user input and skip iteration ad hoc
        if not inputs.is_user_input_valid_ints(current_move_tile) or not board.is_tile_valid(int(current_move_tile)):
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
        winner = make_move_response[winner_str]
        status = make_move_response[status_str]
        
        # show board, update turn
        if current_tile_turn == bot_tile:
            print("Bot (O) has made a move to tile " + current_move_tile + ".")
        board.print_board(board_dict)
        current_tile_turn = update_turn(current_tile_turn)
        
    # end of game, print the winner, prompt game restart
    inputs.print_game_winner(status, winner)
    inputs.prompt_restart()

# update whose turn
# RETURNS: 'X' or 'O' as strings
def update_turn(current_tile_turn: str) -> str:
    if current_tile_turn == player_tile:
        return bot_tile
    return player_tile

# this is the driver
if __name__ == "__main__":
    inputs.start_prompt()