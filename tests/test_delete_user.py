import requests



id = 2


def test_delete_user(url):
    response = requests.delete(f'{url}/api/users/{id}')
    assert response.status_code == 204
