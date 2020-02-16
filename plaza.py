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

app = Flask(__name__)
app.config['SECRET_KEY'] = "the hardest string to guess 3v4r"

bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        # save entered name
        session['name'] = form.name.data
        # flash a message
        flash('Great! We hope you enjoy the community')
        # clear input
        return redirect(url_for('home'))
    return render_template('home.html', form=form, name=session.get('name'))


@app.route('/shopper/<shopper_name>')
def shopper(shopper_name):
    return render_template('shopper.html', shopper_name=shopper_name)


@app.route('/store/<store_name>')
def store(store_name):
    return render_template('store.html', store_name=store_name)


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
