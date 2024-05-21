import requests
from jsonschema import validate
from schemas.project import get_users


id = 2
invalid_id = 23


def test_get_user(url):
    response = requests.get(f'{url}/api/users/{id}')
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=get_users)


def test_resource_not_found(url):
    response = requests.get(f'{url}/api/unknown/{invalid_id}')
    assert response.status_code == 404
    assert response.json() == {}
