import board

# this file holds all methods relatd to user inputs

def print_game_start_text() -> None:
    print("For your reference, this is what your input will look like: 1-9 like a numpad.")
    board.print_index_board()
    print("\n\n")


# make sure that user input is either 1 or 2
# RETURNS: True if valid input, False if otherwise
def is_user_input_valid_ints(user_input: str) -> int:
    try:
        user_input = int(user_input)
    except ValueError:
        return False
    return True

# makes sure that user input is Y/y/N/n for game restart
def is_user_input_valid_restart(user_input: str) -> int:
    try:
        user_input == "y" or user_input == "Y" or user_input == "n" or user_input == "N"
    except ValueError:
        return False
    return True


# prompts the user for choice of game with error handling
# RETURNS: 1 or 2
def get_user_input_game_type() -> int:
    print("Welcome to a game of TicTacToe!\n")
    prompt = "Do you want to play against the computer? (1)\nOr watch an AI play against the computer? (2)\n"
    on_validation_error = "ERROR: Invalid input. Please type either 1 or 2.\n"
    while True:
        value = input(prompt)

        if is_user_input_valid_ints(value):
            return int(value) == 1 or int(value) == 2
        print(on_validation_error)

# handle game outcome
# RETURNS: None
def print_game_winner(status: str, winner: str) -> None:
    if status == "COMPLETE":
        if winner == "TIE":
            print("Game ended in a tie. GG")
        else:
            print(winner + " is the winner. GG")
    else:
        print("Hmm, the game status should be complete, but isn't. Sorry.")