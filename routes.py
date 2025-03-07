from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
@jwt_required()
def test():
    current_user = get_jwt_identity()
    return jsonify({"message": "API Çalışıyor!", "user": current_user})
