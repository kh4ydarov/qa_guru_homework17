import requests


url = "https://reqres.in"
id = 2


def test_delete_user():
    response = requests.delete(f'{url}/api/users/{id}')
    assert response.status_code == 204
