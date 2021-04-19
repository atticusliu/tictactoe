import board
import main

# this file holds all logic related to the bot

# RETURNS: string of the best possible move for the computer
def get_best_bot_move(board_dict: dict) -> str:
    best_score = -800
    best_move = 0

    # go through each open space and determine scores
    for current_tile in board_dict:
        if board_dict[current_tile] == main.empty_tile:
            board_dict[current_tile] = main.bot_tile
            score = minimax(board_dict, 0, False)
            board_dict[current_tile] = main.empty_tile

            if score > best_score:
                best_score = score
                best_move = current_tile

    return str(best_move)

# RETURNS bool if there's a draw
def check_draw(board_dict: dict) -> bool:
    for current_tile in board_dict:
        if (board_dict[current_tile] == main.empty_tile):
            return False
    return True

# recursively go and find the best move
# RETURNS: the tile of the best move
def minimax(board_dict: dict, depth: int, is_maximizing: bool) -> int:
    if board.check_for_winner(board_dict, main.bot_tile):
        return 1
    elif board.check_for_winner(board_dict, main.player_tile):
        return -1
    elif check_draw(board_dict):
        return 0
  
    # computer will be the maximized
    if is_maximizing:
        best_score = -800

        for current_tile in board_dict:
            if board_dict[current_tile] == main.empty_tile:
                board_dict[current_tile] = main.bot_tile
                score = minimax(board_dict, depth+1, False)
                board_dict[current_tile] = main.empty_tile

                best_score = max(best_score, score)
        return best_score
    # player will be the minimized
    else:
        best_score = 800

        # go through each open space and determine scores
        for current_tile in board_dict:
            if board_dict[current_tile] == main.empty_tile:
                board_dict[current_tile] = main.player_tile
                score = minimax(board_dict, depth+1, True)
                board_dict[current_tile] = main.empty_tile

                best_score = min(best_score, score)
        return best_score