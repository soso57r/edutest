def test_root_endpoint_returns_ok(client):
    # Given
    endpoint = '/'

    # When
    response = client.get(endpoint)

    # Then
    assert response.status_code == 200
    assert response.data == b'ok'
