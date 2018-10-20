def test_basic(client):
    req = client.get('/')
    assert req.status_code == 200
    assert req.data == b"Hello, World!"
