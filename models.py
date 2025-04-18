from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, autoincrement=True, primary_key=True)
    username = db.Column("username",db.String(80), unique=True, nullable=False)
    password_hash = db.Column("password",db.String(256), nullable=False)
    role = db.Column("role",db.String(20), default="user") 

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
