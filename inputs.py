import board
import game

# this file holds all methods relatd to user inputs

# start prompt asking the user to choose the type of game that'll be played
# pretty major driver of logic, too
# RETURNS: None
def start_prompt() -> None:
    # game_type will be either 1 or 2
    game_type = get_user_input_game_type()

    if game_type == 1:
        print("Let's start a user vs. computer game!")
        game.start_game()
    elif game_type == 2:
        print("UNDER CONSTRUCTION")
        #print("Let's watch an AI vs computer game!")
        #game.start_game()

# prints out sample board for user
# RETURNS: None
def print_game_start_text() -> None:
    print("For your reference, this is what your input will look like: 1-9 like a numpad.")
    board.print_index_board()
    print("\n\n")

# verifies user input can be cast to int 
# RETURNS: True if valid input, False if otherwise
def is_user_input_valid_ints(user_input: str) -> bool:
    try:
        user_input = int(user_input)
    except ValueError:
        return False
    return True

# makes sure that user input is Y/y/N/n for game restart
# RETURNS: bool if Y/y/N/n
def is_user_input_valid_restart(user_input: str) -> bool:
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
    on_validation_error = "ERROR: Please type either 1 or 2.\n"
    while True:
        value = input(prompt)

        if is_user_input_valid_ints(value) and (int(value) == 1 or int(value) == 2):
            return int(value)
        print(on_validation_error)

# RETURNS player's move
def player_move() -> str:
    return input("It is your (X)'s turn. Make a move: Enter 1-9 (inclusive): ")

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

# handles game restart logic
# RETURNS: None
def prompt_restart() -> None:
    restart = input("Do you want to play again? (Y/N): ")
    while is_user_input_valid_restart(restart):
        if restart == "Y" or restart == "y":
            start_prompt()
        elif restart == "N" or restart == "n":
            exit()
        else:
            restart = input("Try again with Y/N: ")
