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


app = Flask(__name__)
app.config =

db = SQLAlchemy(app)
from models import Role, Fan
migrate = Migrate(app, db)

bootstrap = Bootstrap(app)




@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Fan=Fan, Role=Role)




if __name__ == '__main__':
    app.run(debug=True)
