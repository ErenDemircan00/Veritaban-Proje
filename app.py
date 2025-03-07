from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')

def index():
    # Veritabanına bağlantı
    connection = mysql.connector.connect(
        host='localhost',  # Veritabanı sunucusu, localhost yerel bilgisayarınız için
        user='root',       # Kullanıcı adı, 'root' ise root kullanabilirsiniz
        password='şifreniz',  # Veritabanı şifrenizi buraya yazın
        database='veritabanı_adınız'  # Bağlanmak istediğiniz veritabanı adı
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table_name")  # Burada sorgu yapıyoruz
    result = cursor.fetchall()  # Sorgudan dönen tüm verileri alıyoruz
    connection.close()  # Bağlantıyı kapatıyoruz
    
    return str(result)  # Sonuçları ekrana yazdırıyoruz

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
