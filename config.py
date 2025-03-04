class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://kullanici_adi:sifre@localhost/veritabani_adi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'supergizlisifre'  # JWT için gizli anahtar
