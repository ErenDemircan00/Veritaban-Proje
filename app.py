from flask import Flask, render_template, request
import mysql.connector
from models import db
from config import Config
from my_routes import api_bp



#jwt = JWTManager(app)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(api_bp)
    db.init_app(app)
    
    return app

app = create_app()
# def index(): 


#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form.get('name')
#     return f"Hoşgeldiniz, {name}!"

# if __name__ == '__main__':
#     app.run(debug=True)
