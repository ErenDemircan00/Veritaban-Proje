import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Config sınıfı
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')

# Flask uygulaması
class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.db = SQLAlchemy(self.app)
        self.bcrypt = Bcrypt(self.app)
        self.jwt = JWTManager(self.app)
        self.limiter = Limiter(get_remote_address, app=self.app, default_limits=["5 per minute"])

    def register_blueprints(self):
        from routes import api_bp
        from auth import auth_bp
        self.app.register_blueprint(api_bp, url_prefix='/api')
        self.app.register_blueprint(auth_bp, url_prefix='/auth')

    def run(self):
        with self.app.app_context():
            self.db.create_all()
        self.app.run(debug=True)

# Uygulamayı çalıştır
if __name__ == '__main__':
    flask_app = FlaskApp()
    flask_app.register_blueprints()
    flask_app.run()