from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response,session
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from functools import wraps
import os
import jwt
import datetime
import pytz
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY","12345")
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)
bcrypt = Bcrypt(app)
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'token' in request.cookies:
            token = request.cookies.get('token')
        elif 'Authorization' in request.headers:
            auth_header = request.headers.get('Authorization')
            if auth_header.startswith('Bearer '):
                token = auth_header[7:] 
        
        if not token:
            if request.headers.get('Content-Type') == 'application/json':
                return jsonify({'message': 'Token eksik!'}), 403
            return redirect(url_for('login'))
        
        try:
            data = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            current_user = {'id': data['user_id'], 'username': data['username']}
        except:
            if request.headers.get('Content-Type') == 'application/json':
                return jsonify({'message': 'Geçersiz token!'}), 403
            return redirect(url_for('login'))
            
        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/')
def index():
    username = session.get('username')
    return render_template('index.html', username=username)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        hashed_password = bcrypt.generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
                     (username, hashed_password, email))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()
    
        is_api = request.headers.get('Content-Type') == 'application/json'
        
        if is_api:
            data = request.get_json()
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, username, password FROM users WHERE username = %s", [username])
        user = cursor.fetchone()
        cursor.close()

        if user:
            user_id, user_name, hashed_password = user
            if bcrypt.check_password_hash(hashed_password, password):
                token = jwt.encode({
                    'user_id': user_id,
                    'username': user_name,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                }, app.secret_key, algorithm='HS256')
                
                session['username'] = user_name
                
                if is_api:
                    return jsonify({'message': 'Giriş başarılı', 'token': token})
                else:
                    response = make_response(redirect(url_for('tokenPage')))
                    response.set_cookie('token', token, httponly=True, max_age=7200)
                    return response
            else:
                if is_api:
                    return jsonify({'message': 'Geçersiz şifre'}), 401
                else:
                    return render_template('login.html', error='Geçersiz şifre')
        
        if is_api:
            return jsonify({'message': 'Kullanıcı bulunamadı'}), 401
        else:
            return render_template('login.html', error='Kullanıcı bulunamadı')
    
    return render_template('login.html')

@app.route('/tokenPage')
@token_required
def tokenPage(current_user):
    token = request.cookies.get('token')
    return render_template('TokenPage.html',token=token)


@app.route('/logout')
def logout():
    session.clear()
    response = make_response(redirect(url_for('login')))
    response.set_cookie('token', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
