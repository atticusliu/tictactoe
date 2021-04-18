import requests
import json
import api_calls
import auth
import board
import inputs

# This file holds the guts of the program

# actual game mechanics
def start_game() -> None:
    board_dict = {
        '7': ' ', '8': ' ', '9': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '1': ' ', '2': ' ', '3': ' '
    }
    
    # setup new game and verify echo API responses are good
    api_key, game_id = auth.set_up_and_auth_new_game()

    # new game status is NONE, but I'm gonna overwrite it to "Active". Initialize winner, start game with X
    status = 'ACTIVE'
    winner = ''
    current_tile_turn = 'X'

    # print text, board before start of game
    inputs.print_game_start_text()
    board.print_board(board_dict)

    # use game status
    while status == 'ACTIVE':
        current_move_spot = input("It is " + current_tile_turn + "'s turn. Make a move: Enter 1-9 (inclusive): ")
        
        # sanitize user input and skip iteration ad hoc
        if not inputs.is_user_input_valid_ints(current_move_spot) or not board.is_spot_valid(int(current_move_spot)) or board_dict[current_move_spot] != ' ':
            print("Invalid input or the spot has been taken. Please try again.")
            continue

        # if spot is open, go for it
        elif board_dict[current_move_spot] == ' ':
            board_dict[current_move_spot] = current_tile_turn

            x, y = board.get_x_y_from_spot(current_move_spot)
            make_move_response = api_calls.make_move(api_key, game_id, x, y, current_tile_turn).json()
            # update things after each successful move
            winner = make_move_response['winner']
            status = make_move_response['status']
        
        # show board, update turn
        board.print_board(board_dict)
        current_tile_turn = update_turn(current_tile_turn)
        
    # end of game, print the winner
    inputs.print_game_winner(status, winner)

    # restart game? 
    restart = input("Do you want to play again? (Y/N): ")
    if inputs.is_user_input_valid_restart(restart):
        if restart == "Y" or restart == "y":
            start_game()

# update whose turn
# RETURNS: 'X' or 'O' as strings
def update_turn(current_tile_turn: str) -> str:
    if current_tile_turn =='X':
        current_tile_turn = 'O'
    else:
        current_tile_turn = 'X'
    return current_tile_turn

# kick things off
if __name__ == "__main__":
    # game_type will be either 1 or 2
    game_type = inputs.get_user_input_game_type()

    if game_type == 1:
        print("Let's start a user vs. computer game!")
        start_game()
    else:
        print("UNDER CONSTRUCTION")