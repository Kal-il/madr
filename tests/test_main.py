from http import HTTPStatus

from fastapi.testclient import TestClient

from madr.main import app


def test_main_must_return_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'ola, mundo'}
