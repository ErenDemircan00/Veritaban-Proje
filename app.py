from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')

def index():
    # Veritabanına bağlantı
    connection = mysql.connector.connect(
        host='localhost',  # Veritabanı sunucusu, localhost yerel bilgisayarınız için
        user='root',       # Kullanıcı adı, 'root' ise root kullanabilirsiniz
        password='',  # Veritabanı şifrenizi buraya yazın
        database='flask_veritabani'  # Bağlanmak istediğiniz veritabanı adı
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM User")  # Burada sorgu yapıyoruz
    result = cursor.fetchall()  # Sorgudan dönen tüm verileri alıyoruz
    connection.close()  # Bağlantıyı kapatıyoruz
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return f"Hoşgeldiniz, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
