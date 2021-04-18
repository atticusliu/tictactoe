import requests
import json

# This file holds the methods used to call the APIs provided to me

base_url = "http://127.0.0.1:5000"

# calls GET /key
# RETURNS: API key string or something failure-related
def get_api_key() -> str:
    # get an API key via text
    try:
        api_key = requests.get(base_url+"/key")
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return api_key

# calls GET /echo
# RETURNS: OK or something failure-related
def get_echo(api_key: str) -> str:
    headers = {"api-key": api_key}

    try:
        echo_response = requests.get(base_url+"/echo", headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return echo_response


# calls GET /echo/auth
# RETURNS: OK auth or something failure-related
def get_echo_auth(api_key: str) -> str:
    headers = {"api-key": api_key}

    try:
        echo_auth_response = requests.get(base_url+"/echo/auth", headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return echo_auth_response

# calls POST /game
# RETURNS: JSON with game_id, winner, status, gameboard
def post_game_create(api_key: str) -> json:
    headers = {"api-key": api_key}

    try: 
        game_create_response = requests.post(base_url+"/game", headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    return game_create_response

# calls GET /game/{game_id}
# RETURNS: JSON with game_id, winner, status, gameboard
def get_game(api_key: str, game_id: str) -> json:
    headers = {"api-key": api_key}

    try:
        get_game_response = requests.get(base_url+"/game/"+game_id, headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return get_game_response

# calls PUT /game/{game_id}/move
# RETURNS: JSON with game_id, winner, status, gameboard
def make_move(api_key: str, game_id: str, x: str, y: str, tile:str) -> json:
    headers = {"api-key": api_key}
    url_query_string = "?x="+x+"&y="+y+"&tile="+tile
    
    try:
        put_game_move_response = requests.put(base_url+"/game/"+game_id+"/move"+url_query_string, headers=headers)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    
    return put_game_move_response