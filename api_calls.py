import requests
import json

# This file holds the methods used to call the APIs provided to me

# globals. Also note server runs locally
base_url = "http://127.0.0.1:5000"
api_key_str = "api-key"
key_str = "/key"
echo_str = "/echo"
echo_auth_str = echo_str + "/auth"
game_str = "/game"
game_str_back = "/game/"
move_str = "/move"
user_friendly_error_message = "Can't connect to server. Sorry. Check back later."

# calls GET /key
# RETURNS: API key string or something failure-related
def get_api_key() -> str:
    # get an API key via text
    try:
        api_key = requests.get(base_url + key_str)
    except:
        raise SystemExit(user_friendly_error_message)

    return api_key

# calls GET /echo
# RETURNS: OK or something failure-related
def get_echo(api_key: str) -> str:
    headers = {api_key_str: api_key}

    try:
        echo_response = requests.get(base_url + echo_str, headers=headers)
    except:
        raise SystemExit(user_friendly_error_message)

    return echo_response


# calls GET /echo/auth
# RETURNS: OK auth or something failure-related
def get_echo_auth(api_key: str) -> str:
    headers = {api_key_str: api_key}

    try:
        echo_auth_response = requests.get(base_url + echo_auth_str, headers=headers)
    except:
        raise SystemExit(user_friendly_error_message)

    return echo_auth_response

# calls POST /game
# RETURNS: JSON with game_id, winner, status, gameboard
def post_game_create(api_key: str) -> json:
    headers = {api_key_str: api_key}

    try: 
        game_create_response = requests.post(base_url + game_str, headers=headers)
    except:
        raise SystemExit(user_friendly_error_message)

    return game_create_response

# calls GET /game/{game_id}
# RETURNS: JSON with game_id, winner, status, gameboard
def get_game(api_key: str, game_id: str) -> json:
    headers = {api_key_str: api_key}

    try:
        get_game_response = requests.get(base_url + game_str_back + game_id, headers=headers)
    except:
        raise SystemExit(user_friendly_error_message)
    
    return get_game_response

# calls PUT /game/{game_id}/move
# RETURNS: JSON with game_id, winner, status, gameboard
def make_move(api_key: str, game_id: str, x: str, y: str, tile:str) -> json:
    headers = {api_key_str: api_key}
    # can make these strings global as well
    url_query_string = "?x="+x+"&y="+y+"&tile="+tile
    
    try:
        put_game_move_response = requests.put(base_url + game_str_back + game_id+ move_str + url_query_string, headers=headers)
    except:
        raise SystemExit(user_friendly_error_message)
    
    return put_game_move_response