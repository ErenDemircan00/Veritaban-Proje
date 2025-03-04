from flask import Flask
from config import Config
from db import db
from routes import api_bp
from auth import auth_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

# JWT Yönetimi
jwt = JWTManager(app)

# Veritabanı bağlantısını başlat
db.init_app(app)

# API Blueprint'leri ekle
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
