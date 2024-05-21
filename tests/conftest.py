import pytest


@pytest.fixture(scope='function')
def url():
    return "https://reqres.in"