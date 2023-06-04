import requests
import random
from faker import Faker

fake = Faker()
random_name = fake.name()

host = "https://pokemonbattle.me:9104"

# Создать покемона
create_url = f"{host}/pokemons"
photo_number = random.randint(1, 1000)
photo_url = f"https://dolnikov.ru/pokemons/albums/{photo_number:03d}.png"

body_data = {
    "name": random_name,
    "photo": photo_url
}

headers = {
    "trainer_token": "c4d8f227a79ecf5dbe8b224086edcb74"
}

create_response = requests.post(create_url, json=body_data, headers=headers)
create_data = create_response.json()
pokemon_id = create_data["id"]

print(create_response.text)

# Обновить покемона
update_url = f"{host}/pokemons"
photo_number = random.randint(1, 1000)
photo_url = f"https://dolnikov.ru/pokemons/albums/{photo_number:03d}.png"

body_data = {
    "pokemon_id": pokemon_id,
    "name": random_name,
    "photo": photo_url
}

update_response = requests.put(update_url, json=body_data, headers=headers)
print(update_response.text)

# Добавить покемона в покебол
add_pokeball_url = f"{host}/trainers/add_pokeball"
body_data = {
    "pokemon_id": pokemon_id
}

add_pokeball_response = requests.post(add_pokeball_url, json=body_data, headers=headers)
print(add_pokeball_response.text)
