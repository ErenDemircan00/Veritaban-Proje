from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')

def index():
    # Veritabanına bağlantı
    connection = mysql.connector.connect(
        host='localhost',  
        user='root',       
        password='',  
        database='flask_veritabani'  
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Kullanicilar") 
    result = cursor.fetchall()  
    connection.close()  
    
    return str(result) 

if __name__ == '__main__':
    app.run(debug=True)

def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Hoşgeldiniz, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
