from flask import render_template, url_for, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from . import auth
from .forms import LoginForm, RegistrationForm
from ..email import send_email
from ..models import User
from .. import db


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # We don't want user to see this page if they are already logged in
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.home')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out.")
    return redirect(url_for('main.home'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                   username=form.username.data,
                   password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Coolio. Now you can login.")
        # since form input is valid (not an existing user, etc),
        # we can send them a welcome email
        send_email(form.email.data,
                    'Welcome to Ragtime!',
                    'mail/welcome',
                    user=user)
        flash("We sent you a confirmation email! Click the link in the email to confirm your account.")
        send_email(form.email.data,
                    'Confirm Your Account',
                    'auth/email/confirm',
                    user=user,
                    token=user.generate_confirmation_token())
        if current_app.config['RAGTIME_ADMIN']:
            send_email(current_app.config['RAGTIME_ADMIN'],
                        'New User',
                        'mail/new_user',
                        user=user)
        return redirect(url_for('main.home'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        flash("You're already confirmed, silly!")
        return redirect(url_for('main.home'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account! Thank you.')
    else:
        flash("Whoops! That confirmation link either expired, or it isn't valid.")
    return redirect(url_for('main.home'))


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        # ? we add check for endpoint is something in profile section
        if not current_user.confirmed \
                and request.endpoint \
                and request.blueprint != 'auth' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.home'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email,
        'Confirm Your Account',
        'auth/email/confirm',
        user=current_user,
        token=token)
    current_app.logger.debug("Resent confirmation email")
    flash("We sent a new confirmation email! Please check your inbox.")
    return redirect(url_for('main.home'))