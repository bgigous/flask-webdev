from flask import session, render_template, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import Fan, Role

@main.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        name_entered = form.name.data
        fan = Fan.query.filter_by(username=name_entered).first()
        if fan is None:
            fan = Fan(username=name_entered)
            db.session.add(fan)
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


@main.route('/fan/<fan_name>')
def fan(fan_name):
    return render_template('fan.html', fan_name=fan_name)


@main.route('/base')
def base():
    return render_template('base.html')

"""
@main.route('/artist/<artist_name>')
def artist(artist_name):
    return render_template('artist.html', artist_name=artist_name)
"""
