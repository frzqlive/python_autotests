import requests
import pytest

host = "https://pokemonbattle.me:9104"

def test_status_code():
    url = f"{host}/trainers"
    response = requests.get(url)
    assert response.status_code == 200

def test_check_response():
    url = f"{host}/trainers?trainer_id=4271"
    response = (requests.get(url)).json()
    assert response["trainer_name"] == "chelovek-pauk"