import board

# this file holds all the logic regarding the computer's logic

comp_tile = 'O'
player_tile = 'X'
empty_tile = ' '

# MINIMAX logic will drive the computer
def central_computer_logic_move(board_dict: dict) -> str:
    best_score = -800
    best_move = 0

    # go through each open space and determine scores
    for current_spot in board_dict:
        if board_dict[current_spot] == empty_tile:
            board_dict[current_spot] = comp_tile
            score = minimax(board_dict, 0, False)
            board_dict[current_spot] = empty_tile

            if score > best_score:
                best_score = score
                best_move = current_spot

    return str(best_move)

def check_draw(board_dict: dict) -> bool:
    for current_tile in board_dict:
        if (board_dict[current_tile] == empty_tile):
            return False
    return True

def minimax(board_dict: dict, depth: int, is_maximizing: bool) -> int:
    if board.check_for_winner(board_dict, comp_tile):
        return 1
    elif board.check_for_winner(board_dict, player_tile):
        return -1
    elif check_draw(board_dict):
        return 0
  
    # computer will be the maximized
    if is_maximizing:
        best_score = -800

        for current_spot in board_dict:
            if board_dict[current_spot] == empty_tile:
                board_dict[current_spot] = comp_tile
                score = minimax(board_dict, depth+1, False)
                board_dict[current_spot] = empty_tile

                best_score = max(best_score, score)
        return best_score
    # player will be the minimized
    else:
        best_score = 800

        # go through each open space and determine scores
        for current_spot in board_dict:
            if board_dict[current_spot] == empty_tile:
                board_dict[current_spot] = player_tile
                score = minimax(board_dict, depth+1, True)
                board_dict[current_spot] = empty_tile

                best_score = min(best_score, score)
        return best_score

