from flask import session, render_template, redirect, url_for, flash, current_app
from . import main
from .forms import NameForm
from .. import db
from ..models import User, Role
from ..email import send_email

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


# Not included until later, in user roles or something
# TODO: Gotta decide what to do here
@main.route('/<fan_name>')
def fan(fan_name):
    return render_template('fan.html', fan_name=fan_name)
