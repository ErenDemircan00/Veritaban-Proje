from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')  # Varsayılan olarak "user"

    if not username or not password:
        return jsonify({"error": "Kullanıcı adı ve şifre gereklidir"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Bu kullanıcı adı zaten alınmış"}), 400

    new_user = User(username=username, role=role)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Kullanıcı başarıyla oluşturuldu"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity={"username": username, "role": user.role}, expires_delta=timedelta(minutes=15))
        refresh_token = create_refresh_token(identity=username, expires_delta=timedelta(days=7))
        return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

    return jsonify({"error": "Geçersiz kullanıcı adı veya şifre"}), 401
