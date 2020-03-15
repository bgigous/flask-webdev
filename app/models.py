from datetime import datetime
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as WebSerializer
from . import db
from . import login_manager


class Permission:
    """
    Permission model for defining permissions of the app
        FOLLOW - User can follow other users
        REVIEW - User can write reviews for compositions
        PUBLISH - Uesr can publish compositions
        MODERATE - User can moderate reviews (edit, delete)
        ADMIN - User can do everything
    """
    FOLLOW = 1
    REVIEW = 2
    PUBLISH = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    # XXX: Why doesn't this set permissions to 0? default=0
    permissions = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.permissions is None:
            self.permissions = 0

    @staticmethod
    def insert_roles():
        roles = {
            'User':             [Permission.FOLLOW, Permission.REVIEW, Permission.PUBLISH],
            'Moderator':        [Permission.FOLLOW, Permission.REVIEW, Permission.PUBLISH,
                                 Permission.MODERATE],
            'Administrator':    [Permission.FOLLOW, Permission.REVIEW, Permission.PUBLISH,
                                 Permission.MODERATE, Permission.ADMIN],
        }
        default_role = 'User'
        for r in roles:
            # see if role is already in table
            role = Role.query.filter_by(name=r).first()
            if role is None:
                # it's not so make a new one
                role = Role(name=r)
            role.reset_permissions()
            # add whichever permissions the role needs
            for perm in roles[r]:
                role.add_permission(perm)
            # if role is the default one, default is True
            role.default = (role.name == default_role)
            # add new role
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return f'<Role {self.name}>'

    def add_permission(self, perm):
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permissions(self):
        self.permissions = 0

    def has_permission(self, perm):
        # Use bitwise AND to see if perm present
        return self.permissions & perm == perm


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    # Artist info
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    bio = db.Column(db.Text())
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # For the first time a user logs in, we'll set their role
        # The next time they log in they will skip this
        # TODO: Explain, how can we do this??? self.role hasn't been defined yet
        if self.role is None:
            # if the User has email that matches admin email, automatically
            # make that User an Administrator by giving them that role
            if self.email == current_app.config['RAGTIME_ADMIN']:
                self.role = Role.query.filter_by(name='Administrator').first()
            # otherwise, it's just a plain old user
            if self.role == None:
                self.role = Role.query.filter_by(default=True).first()

    def __repr__(self):
        return f'<User {self.username}>'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration_sec=3600):
        s = WebSerializer(current_app.secret_key, expiration_sec)
        return s.dumps({'confirm_id': self.id}).decode('utf-8')

    def confirm(self, token):
        s = WebSerializer(current_app.secret_key)
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        # Matches the logged in user
        if data.get('confirm_id') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        # Don't commit yet! We'll make sure it's legit when we go to the /commit page
        return True

    # Simple check for if a user can do something
    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    # Because it's very common to check for admin
    def is_administrator(self):
        return self.can(Permission.ADMIN)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()


class AnonymousUser(AnonymousUserMixin):
    def can(self, perm):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
