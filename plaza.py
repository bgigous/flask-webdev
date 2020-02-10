from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html', name='Bob')


@app.route('/shopper/<shopper_name>')
def shopper(shopper_name):
    return render_template('shopper.html', shopper_name=shopper_name)


@app.route('/store/<store_name>')
def store(store_name):
    return render_template('store.html', store_name=store_name)


@app.errorhandler(404)
def page_not_found(e):
    error_msg="That page doesn't exist"
    return render_template('error.html', error_msg=error_msg), 404


@app.errorhandler(500)
def internal_server_error(e):
    error_msg="Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html", error_msg=error_msg), 500


if __name__ == '__main__':
    app.run(debug=True)
