import requests
from jsonschema import validate
from schemas.project import update_user_put

id = 2


def test_update_user(url):
    response = requests.put(f'{url}/api/users/{id}', data={"name": "test", "job": "test"})
    body = response.json()
    assert response.status_code == 200
    assert response.json()['name'] == 'test'
    validate(body, schema=update_user_put)