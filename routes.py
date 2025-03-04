from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/test', methods=['GET'])
def test():
    return {"message": "API Çalışıyor!"}
