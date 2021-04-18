import board

# this file holds all the logic regarding the computer's logic

comp_tile = 'O'
player_tile = 'X'
empty_tile = ' '

# MINIMAX logic will drive the computer
def central_computer_logic_move(board_dict: dict, x: str) -> str:
    best_score = -1000
    best_move = 0

    # go through each open space and determine scores
    for current_spot in board_dict:
        if board.is_space_free(board_dict, current_spot):
            board_dict[current_spot] = x
            score = minimax(board_dict, 0, False)
            board_dict[current_spot] = empty_tile

            if score > best_score:
                best_score = score
                best_move = current_spot

    return str(best_move)

def minimax(board_dict: dict, depth: int, is_maximizing: bool) -> int:
    is_comp_winner = board.check_for_winner(board_dict, comp_tile)
    is_player_winner = board.check_for_winner(board_dict, player_tile)

    if is_comp_winner:
        return 1
    elif is_player_winner:
        return -1
    # tie scenario
    elif not is_comp_winner and not is_player_winner:
        return 0

    # check is_maximizing
    if is_maximizing:
        best_score = -1000

        # go through each open space and determine scores
        for current_spot in board_dict:
            if board.is_space_free(board_dict, current_spot):
                board_dict[current_spot] = comp_tile
                score = minimax(board_dict, depth+1, False)
                board_dict[current_spot] = empty_tile

                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 1000

        # go through each open space and determine scores
        for current_spot in board_dict:
            if board.is_space_free(board_dict, current_spot):
                board_dict[current_spot] = player_tile
                score = minimax(board_dict, depth+1, True)
                board_dict[current_spot] = empty_tile

                if score < best_score:
                    best_score = score
        return best_score

