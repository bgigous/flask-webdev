from ragtime import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Fan', backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name


class Fan(db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #email = db.Column(db.String(64), unique=True, index=True)
    #password = db.Column(db.String(64), unique=True, index=True)


    def __repr__(self):
        return '<Fan %r>' % self.username
