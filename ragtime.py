import os
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask import session
from flask import redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "the hardest string to guess 3v4r"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Role, Fan
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Fan=Fan, Role=Role)


@app.route('/', methods=['GET', 'POST'])
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
        return redirect(url_for('home'))
    return render_template(
        'home.html',
        form=form,
        name=session.get('name'),
        # If known exists otherwise return false
        known=session.get('known', False))


@app.route('/fan/<fan_name>')
def fan(fan_name):
    return render_template('fan.html', fan_name=fan_name)


@app.route('/artist/<artist_name>')
def artist(artist_name):
    return render_template('artist.html', artist_name=artist_name)


@app.errorhandler(404)
def page_not_found(e):
    error_msg="That page doesn't exist."
    return render_template('error.html', error_msg=error_msg), 404


@app.errorhandler(500)
def internal_server_error(e):
    error_msg="Sorry, we seem to be experiencing some technical difficulties. Please try again later."
    return render_template("error.html", error_msg=error_msg), 500

if __name__ == '__main__':
    app.run(debug=True)
