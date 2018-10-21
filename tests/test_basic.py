def test_app_init(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"ok" in rv.data


def test_blueprint_init(client):
    rv = client.get('/api', follow_redirects=True)
    assert rv.status_code == 200
    assert rv.data == b"Hello, World!"
