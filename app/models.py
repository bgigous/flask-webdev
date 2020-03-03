from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Fan', backref='role')

    def __repr__(self):
        return f'<Role {self.name}>'


class Fan(UserMixin, db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    #password = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f'<Fan {self.username}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return Fan.query.get(int(user_id))



"""
class Manager(Fan):
    __tablename__ = 'managers'
    fan_id = db.Column(db.Integer, db.ForeignKey('fans.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))


class Artist(Fan):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(64), unique=True, index=True)
    display_name = db.Column(db.String(64), unique=False)

    def __repr__(self):
        return f'<Artist {self.alias}>'
"""