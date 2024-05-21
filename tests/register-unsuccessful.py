import requests
from jsonschema import validate
from schemas.schemas import register_unsuccessful

url = "https://reqres.in"


def test_put_user():
    response = requests.post(f'{url}/api/register', data={"email": "sydney@fife"})

    body = response.json()
    assert response.status_code == 400
    validate(body, schema=register_unsuccessful)
