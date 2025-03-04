from flask import Flask
from config import Config
from db import db
from routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# Veritabanı bağlantısını başlat
db.init_app(app)

# API Blueprint'i ekleyelim
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
