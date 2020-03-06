import pytest
from app import create_app, db

print("LOADING CONFTEST")

@pytest.fixture(scope='session')
def new_app():
    # setup
    app = create_app('testing')
    app.app_context().push()
    db.create_all()

    # testing begins
    yield app

    # teardown
    db.session.remove()
    db.drop_all()
    app.app_context().pop()