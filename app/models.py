from ragtime import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Fan', backref='role')

    def __repr__(self):
        return f'<Role {self.name}>'


class Fan(db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #email = db.Column(db.String(64), unique=True, index=True)
    #password = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f'<Fan {self.username}>'


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