from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html', name='Bob')


@app.route('/shopper/<shopper_name>')
def shopper(shopper_name):
    return render_template('shopper.html', shopper_name=shopper_name)


@app.route('/store/<store_name>')
def store(store_name):
    return render_template('store.html', store_name=store_name)


if __name__ == '__main__':
    app.run(debug=True)
