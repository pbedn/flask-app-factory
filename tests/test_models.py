from server.models import db, User

create_user = False


class TestModels:
    def test_user_save(self, client):
        """ Test Saving the user model to the database """

        admin = User('admin', 'pass')
        db.session.add(admin)
        db.session.commit()

        user = User.query.filter_by(username="admin").first()
        assert user is not None

    def test_user_password(self, client):
        """ Test password hashing and checking """

        admin = User('admin', 'pass')

        assert admin.username == 'admin'
        assert admin.verify_password('pass')
