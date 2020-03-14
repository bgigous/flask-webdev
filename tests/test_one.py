import pytest
from flask import current_app
from app import create_app, db
from app.models import User, Role
from app.email import send_email

class TestFlaskApp():
    def test_tfa001_uno(self):
        assert True

    def test_tfa002_app_creation(self):
        self.app = create_app('testing')
        assert self.app

    def test_tfa003_current_app(self):
        app = create_app('testing')
        with app.app_context():
            # current_app now defined (or should be)
            assert current_app

    def test_tfa004_current_app2(self):
        app = create_app('testing')
        app.app_context().push()
        # current_app now defined (or should be)
        assert current_app
        assert current_app.config['TESTING']

def test_mine(new_app):
    pass


#@pytest.mark.usefixtures('new_app')
class TestUserAuth():

    def test_tua001_add_user(self, new_app):
        u = User(email='john@example.com', username='john', password='cat')
        db.session.add(u)
        db.session.commit()

    def test_tua002_test_has_hash(self, new_app):
        u = User.query.first()
        assert u.password_hash is not None

    def test_tua003_test_login(self, new_app):
        u = User.query.first()
        assert not u.verify_password('catcat')
        assert u.verify_password('cat')

    def test_tua004_getter_throws(self, new_app):
        u = User.query.first()
        try:
            u.password
            assert False
        except AttributeError:
            pass # passes test if here
        except:
            assert False

    def test_tua005_salt_is_random(self, new_app):
        u1 = User(password="cat")
        u2 = User(password="cat")
        assert u1.password_hash != u2.password_hash

    def test_tua005_token_valid(self, new_app):
        u = User.query.first()
        token = u.generate_confirmation_token()
        assert u.confirm(token)


    # def __del__(self):
    #     teardown(self.app_context)