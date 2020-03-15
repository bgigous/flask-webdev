from flask import session, render_template, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from . import main
from .forms import NameForm, EditProfileForm
from ..models import User, Role, Permission
from ..email import send_email
from ..decorators import admin_required, permission_required

@main.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data

        # DOES THIS STILL BELONG HERE?!@?
        user = User.query.filter_by(username=name_entered).first()
        if user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        # save entered name
        session['name'] = name_entered
        # flash a message
        flash('Great! We hope you enjoy the community')
        # clear input
        form.name.data
        return redirect(url_for('.home'))
    return render_template(
        'home.html',
        form=form,
        name=session.get('name'),
        # If known exists otherwise return false
        known=session.get('known', False))


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', username=username)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Change all user information and then save to database
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        return redirect(url_for('.user', username=current_user.username))
    # Show initial values so user can see what they have already
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.bio.data = current_user.bio
    return render_template('edit_profile.html', form=form)


@main.route('/admin')
@login_required
@admin_required
def admin():
    return "For admins only!"


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def moderate():
    return "For review moderators only!"
