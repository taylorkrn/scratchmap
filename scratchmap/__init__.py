from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from scratchmap.config import Config


#Database
db = SQLAlchemy()
#Encryption of passwords
bcrypt = Bcrypt()
#Login manager to manage logins
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
#Initalise Flask Mail
mail = Mail()

#
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #Initialise Database, Encryption etc. in App
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #Import the blueprints from the packages users, maps, main and errors
    from scratchmap.users.routes import users
    from scratchmap.maps.routes import maps
    from scratchmap.main.routes import main
    from scratchmap.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(maps)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    #Create an app Context
    with app.app_context():
        db.create_all()

    return app
