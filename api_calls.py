import requests
import json

# This module holds the methods used to call the APIs provided to me

# module-level constants. Also note server runs locally
BASE_URL = "http://127.0.0.1:5000"
API_KEY_STR = "api-key"
KEY_STR = "/key"
ECHO_STR = "/echo"
ECHO_AUTH_STR = ECHO_STR + "/auth"
GAME_STR = "/game"
GAME_STR_BACK = "/game/"
MOVE_STR = "/move"
USER_FRIENDLY_ERROR_MESSAGE = "Can't connect to server. Sorry. Check back later."

# calls GET /key
# RETURNS: API key string or something failure-related
def get_api_key() -> str:
    # get an API key via text
    try:
        api_key = requests.get(BASE_URL + KEY_STR)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)

    return api_key

# calls GET /echo
# RETURNS: OK or something failure-related
def get_echo(api_key: str) -> str:
    headers = {API_KEY_STR: api_key}

    try:
        echo_response = requests.get(BASE_URL + ECHO_STR, headers=headers)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)

    return echo_response


# calls GET /echo/auth
# RETURNS: OK auth or something failure-related
def get_echo_auth(api_key: str) -> str:
    headers = {API_KEY_STR: api_key}

    try:
        echo_auth_response = requests.get(BASE_URL + ECHO_AUTH_STR, headers=headers)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)

    return echo_auth_response

# calls POST /game
# RETURNS: JSON with game_id, winner, status, gameboard
def post_game_create(api_key: str) -> json:
    headers = {API_KEY_STR: api_key}

    try: 
        game_create_response = requests.post(BASE_URL + GAME_STR, headers=headers)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)

    return game_create_response

# calls GET /game/{game_id}
# RETURNS: JSON with game_id, winner, status, gameboard
def get_game(api_key: str, game_id: str) -> json:
    headers = {API_KEY_STR: api_key}

    try:
        get_game_response = requests.get(BASE_URL + GAME_STR_BACK + game_id, headers=headers)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)
    
    return get_game_response

# calls PUT /game/{game_id}/move
# RETURNS: JSON with game_id, winner, status, gameboard
def make_move(api_key: str, game_id: str, x: str, y: str, tile:str) -> json:
    headers = {API_KEY_STR: api_key}
    # can make these strings global as well
    url_query_string = "?x="+x+"&y="+y+"&tile="+tile
    
    try:
        put_game_move_response = requests.put(BASE_URL + GAME_STR_BACK + game_id+ MOVE_STR + url_query_string, headers=headers)
    except:
        raise SystemExit(USER_FRIENDLY_ERROR_MESSAGE)
    
    return put_game_move_response