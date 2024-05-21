import requests
from jsonschema import validate
from schemas.project import register_unsuccessful


def test_put_user(url):
    response = requests.post(f'{url}/api/register', data={"email": "sydney@fife"})

    body = response.json()
    assert response.status_code == 400
    validate(body, schema=register_unsuccessful)
