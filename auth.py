import api_calls
# this module holds all things related to authentication

# module-level constants
GAME_ID_STR = 'game_id'
ECHO_RESPONSE_STR = "OK"
ECHO_AUTH_RESPONSE_STR = "Auth OK"
ECHO_RESPONSE_ERROR_MESSAGE = "Echo response is not OK. Quitting."
ECHO_AUTH_RESPONSE_ERROR_MESSAGE = "Echo auth response is not Auth OK. Quitting."

# setup and go through auth
# RETURNS: api_key, game_id tuple
def set_up_and_auth_new_game() -> tuple:
    # fetch API key
    api_key = api_calls.get_api_key().text

    # verify echo calls
    echo_response = api_calls.get_echo(api_key).text

    if echo_response != ECHO_RESPONSE_STR:
        raise ValueError(ECHO_RESPONSE_ERROR_MESSAGE)

    echo_auth_response = api_calls.get_echo_auth(api_key).text

    if echo_auth_response != ECHO_AUTH_RESPONSE_STR:
        raise ValueError(ECHO_AUTH_RESPONSE_ERROR_MESSAGE)

    # create a new game and call .json() on it
    post_game_create_response = api_calls.post_game_create(api_key).json()

    # fetch game_id, status from the JSON above
    game_id = post_game_create_response[GAME_ID_STR]

    return api_key, game_id
