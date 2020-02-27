from flask import render_template, url_for, redirect, url_for, flash, request
from flask_login import login_user
from . import auth
from .forms import LoginForm
from ..models import Fan


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Fan.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/register')
def register():
    pass
