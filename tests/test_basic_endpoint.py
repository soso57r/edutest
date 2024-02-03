import pytest

from edutest import app

def test_root_endpoint_returns_ok(client):
    # Given
    endpoint = '/'

    # When
    response = client.get(endpoint)

    # Then
    assert response.status_code == 200
    assert response.data == b'ok'

def test_increase_endpoint_increases_counter(client):
    # Given
    endpoint = '/inc'
    previous_value = app.counter

    # When
    response = client.post(endpoint)

    # Then
    assert response.status_code == 201
    assert response.json == {
        'msg': 'Successful increase',
        'prev': previous_value,
        'new': previous_value + 1
    }

@pytest.mark.parametrize('nb_inc', (2, 4, 5, 70, 5))
def test_multiple_increase_endpoint_increases_counter_correctly(client, nb_inc):
    # Given
    endpoint = '/inc'
    previous_value = app.counter

    # When
    for _ in range(nb_inc):
        response = client.post(endpoint)

    # Then
    assert response.status_code == 201
    assert response.json == {
        'msg': 'Successful increase',
        'prev': previous_value + nb_inc - 1,
        'new': previous_value + nb_inc
    }

def test_info_endpoint_return_correct_value(client):
    # Given
    endpoint = '/info'

    # When
    response = client.get(endpoint)

    # Then
    assert response.status_code == 200
    assert response.json == {
        'counter': app.counter
    }
