import pytest

from ..server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client
