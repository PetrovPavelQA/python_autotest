import requests
import pytest


token = '539b92575d44d41178f2ff62595eac35' # токен, полученный в боте
host = 'https://api.pokemonbattle.me:9104' # адрес хоста

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 1423})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': 1423})
    response_body = response.json()
    assert response_body['trainer_name'] == 'Diebold'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Diebold')])

def test_tr_name(key,value):
   response = requests.get(f'{host}/trainers', params= {'trainer_id': 1423})
   assert response.json()[key]== value
   #пропустил квадратные скобки в последней строке и долго искал ошибку