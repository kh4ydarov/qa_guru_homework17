import requests
from jsonschema import validate
from schemas.schemas import post_user

url = "https://reqres.in"


def test_create_user():
    response = requests.post(f'{url}/api/users/', data={"name": "test", "job": "test"})

    body = response.json()
    assert response.status_code == 201
    assert response.json()['name'] == 'test'
    validate(body, schema=post_user)
