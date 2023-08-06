import requests

token = '539b92575d44d41178f2ff62595eac35' # токен, полученный в боте
host = 'https://api.pokemonbattle.me:9104' # адрес хоста

response_create_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "kursant",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : token})

response_body = response_create_pokemon.json()
pokemon_id = response_body["id"]  #попытка вытащить id созданного покемона и применить его дальше, что бы не искать руками на сайте 

print(response_create_pokemon.status_code)
print(response_create_pokemon.text)



response_сhangename_pokemon = requests.put(f'{host}/pokemons', json = {
    
    "pokemon_id": pokemon_id,# подставляем id из первого запроса, вроде получилось
    "name": "diversant",
    "photo": "https://dolnikov.ru/pokemons/albums/019.png"
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : token})

print(response_сhangename_pokemon.status_code)
print(response_сhangename_pokemon.text)


response_putpokemon_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": pokemon_id,# подставляем id из первого запроса, вроде получилось
}, headers = {'Content-Type' : 'application/json' , 'trainer_token' : token})

print(response_putpokemon_pokeball.status_code)
print(response_putpokemon_pokeball.text)
