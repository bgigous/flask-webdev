from config import Config
db = SQLAlchemy(app)

def create_app(config_name):
    from .main import main as main_blueprint
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)