import api_calls

# this file holds all things related to authentication

# setup and go through auth
# RETURNS: api_key, game_id tuple
def set_up_and_auth_new_game() -> tuple:
    # fetch API key
    api_key = api_calls.get_api_key().text

    # verify echo calls
    echo_response = api_calls.get_echo(api_key).text

    if echo_response != "OK":
        raise ValueError("Echo response is not OK. Quitting.")

    echo_auth_response = api_calls.get_echo_auth(api_key).text

    if echo_auth_response != "Auth OK":
        raise ValueError("Echo auth response is not Auth OK. Quitting.")

    # create a new game and call .json() on it
    post_game_create_response = api_calls.post_game_create(api_key).json()

    # fetch game_id, status from the JSON above
    game_id = post_game_create_response['game_id']

    return api_key, game_id