import requests
from jsonschema import validate
from schemas.project import post_user


def test_create_user(url):
    response = requests.post(f'{url}/api/users/', data={"name": "test", "job": "test"})

    body = response.json()
    assert response.status_code == 201
    assert response.json()['name'] == 'test'
    validate(body, schema=post_user)
