import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8405f489c55f876b6aaf1b837722e611'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_generate = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "117673",
    "name": 'Yury',
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "117673"
}

'''response_generate = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_generate)
print(response_generate.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''


