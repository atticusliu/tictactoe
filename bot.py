import board
import game

# this module holds all logic related to the bot

# top-level method to fetch best bot move recursively via minimax
# ARGS: board_dict (dict)
# RETURNS: string of the best possible move for the computer
def get_best_bot_move(board_dict: dict) -> str:
    best_score = -800
    best_move = 0

    # go through each open space and determine scores
    for current_tile in board_dict:
        if board.is_tile_free(board_dict, current_tile):
            board_dict[current_tile] = game.BOT_TILE
            score = minimax(board_dict, 0, False)
            board_dict[current_tile] = game.OPEN_TILE

            if score > best_score:
                best_score = score
                best_move = current_tile

    return str(best_move)

# quick method to check for a draw
# ARGS: board_dict (dict)
# RETURNS: bool
def check_draw(board_dict: dict) -> bool:
    for current_tile in board_dict:
        if board.is_tile_free(board_dict, current_tile):
            return False
    return True

# recursively go and find the best move
# ARGS: board_dict (dict), depth (int), is_maximizing (bool)
# RETURNS: int
def minimax(board_dict: dict, depth: int, is_maximizing: bool) -> int:
    if board.check_for_winner(board_dict, game.BOT_TILE):
        return 1
    elif board.check_for_winner(board_dict, game.PLAYER_TILE):
        return -1
    elif check_draw(board_dict):
        return 0
  
    # computer will be the maximized
    if is_maximizing:
        best_score = -800

        for current_tile in board_dict:
            if board.is_tile_free(board_dict, current_tile):
                board_dict[current_tile] = game.BOT_TILE
                score = minimax(board_dict, depth+1, False)
                board_dict[current_tile] = game.OPEN_TILE

                best_score = max(best_score, score)
        return best_score
    # player will be the minimized
    else:
        best_score = 800

        # go through each open space and determine scores
        for current_tile in board_dict:
            if board.is_tile_free(board_dict, current_tile):
                board_dict[current_tile] = game.PLAYER_TILE
                score = minimax(board_dict, depth+1, True)
                board_dict[current_tile] = game.OPEN_TILE

                best_score = min(best_score, score)
        return best_score