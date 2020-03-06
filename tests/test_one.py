import pytest
from flask import current_app
from app import create_app, db

# @pytest.fixture(scope='module')
# def new_app():
#     app = create_app('testing')
#     app_context = app.app_context
#     app_context.push()
#     return app, app_context


# def test_setup():
#     app = create_app('testing')
#     return app


# def test_new_app():
#     app, app_context = new_app()
#     assert current_app is not None

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

print('before use of fixture')

#@pytest.mark.usefixtures('new_app')
class TestUserAuth(new_app):
    def test_tua001_fixture(self):
        assert app
        with app.app_context():
            assert current_app
