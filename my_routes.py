from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
@jwt_required()
def test():
    current_user = get_jwt_identity()
    return jsonify({"message": "API Çalışıyor!", "user": current_user})


@api_bp.route('/test2', methods=['GET'])
def test2():
    user = User.query.get(1)
    print(user.username)
    return jsonify({"message": "API Çalışıyor!"})
