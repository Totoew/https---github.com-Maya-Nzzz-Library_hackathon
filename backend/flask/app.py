from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# ПОДСТАВЬ СВОИ ДАННЫЕ
DB_HOST = "db"  # имя сервиса Postgres в docker-compose
DB_PORT = 5432
DB_USER = "db_user"
DB_PASSWORD = "1234"
DB_NAME = "db_library"

# Подключение к базе
try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME
    )
    print("Connected to Postgres successfully!")
except Exception as e:
    print("Failed to connect to Postgres:", e)

@app.route('/')
def index():
    return jsonify({"message": "Flask app is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
