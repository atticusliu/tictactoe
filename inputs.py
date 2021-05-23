import board
import game

# this module holds all methods relatd to user inputs

# start prompt asking the user to choose the type of game that'll be played
# pretty major driver of logic, too
# ARGS: None
# RETURNS: None
def start_prompt() -> None:
    # game_type will be either 1 or 2
    game_type = get_user_input_game_type()

    if game_type == 1:
        print("Let's start a user vs. computer game!")
        game.start_game()
    elif game_type == 2:
        print("Goodbye.")

# prints out sample board for user
# ARGS: None
# RETURNS: None
def print_game_start_text() -> None:
    print("For your reference, this is what your "
    "input will look like: 1-9 like a numpad.")
    board.print_index_board()
    print("\n\n")

# verifies user input can be cast to int 
# ARGS: user_input (str)
# RETURNS: True if valid input, False if otherwise
def is_user_input_valid_ints(user_input: str) -> bool:
    try:
        user_input = int(user_input)
    except ValueError:
        return False
    return True

# makes sure that user input is Y/y/N/n for game restart
# ARGS: user_input (str)
# RETURNS: bool if Y/y/N/n
def is_user_input_valid_restart(user_input: str) -> bool:
    try:
        (user_input == "y" or user_input == "Y" or
         user_input == "n" or user_input == "N")
    except ValueError:
        return False
    return True

# prompts the user for choice of game with error handling
# ARGS: None
# RETURNS: 1 or 2
def get_user_input_game_type() -> int:
    print("Welcome to a game of TicTacToe!\n")
    prompt = ("Let's play!? (1)\n"
    "Quit (2)\n")
    on_validation_error = "ERROR: Please type either 1 or 2.\n"
    while True:
        value = input(prompt)

        if (is_user_input_valid_ints(value) and
         (int(value) == 1 or int(value) == 2)):
            return int(value)
        print(on_validation_error)

# get player input
# ARGS: None
# RETURNS: str
def player_move() -> str:
    return input("It is your (X)'s turn. Make a move: Enter 1-9 (inclusive): ")

# handles game outcome
# ARGS: status (str), winner (str)
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
# ARGS: None
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
