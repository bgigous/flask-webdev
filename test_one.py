from flask import current_app
from app import create_app, db

def test_setup(self):
    app = create_app('testing')
    self.app_context