class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://kullanici_adi:sifre@localhost/flask_veritabani'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'supergizlisifre'  
