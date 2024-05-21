import requests
from jsonschema import validate
from schemas.schemas import get_users

url = "https://reqres.in"
id = 2
invalid_id = 23


def test_get_user():
    response = requests.get(f'{url}/api/users/{id}')
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=get_users)


def test_resource_not_found():
    response = requests.get(f'{url}/api/unknown/{invalid_id}')
    assert response.status_code == 404
