#JWT-Token

## Gereksinimler
- Python 3.8+
- MySQL
- Git
### 1. Depoyu Klonlayın
```bash
git clone https://github.com/ErenDemircan00//Veritaban-Proje.git
cd dual-db-app/user-management
```
### 2. Sanal Ortam Oluşturun
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
# veya
source venv/bin/activate  # Linux/macOS
```
### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```
### 4. Çevresel Değişkenleri Ayarlayın
Proje kök dizininde .env dosyasını oluşturun:
```.env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=1234
MYSQL_DB=jwt_users
SECRET_KEY=your_secret_key
```
### 5. MySQL Veritabanını Kurun
MySQL’de users veritabanını ve user tablosunu oluşturun:
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### 6. Uygulamayı Çalıştırın
```bash
python app.py
```
