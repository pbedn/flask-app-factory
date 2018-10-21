import pytest

from server import create_app
from server.models import db, User


@pytest.fixture
def client(request):
    app = create_app('server.settings.TestingConfig')
    client = app.test_client()

    db.app = app
    db.create_all()

    if getattr(request.module, "create_user", True):
        admin = User('admin', 'pass')
        db.session.add(admin)
        db.session.commit()

    yield client

    db.session.remove()
    db.drop_all()
