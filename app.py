# app.py
import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    DATABASE_URL = os.environ['DATABASE_URL']
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/test_db')
def test_db():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        result = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"message": "Database connection successful", "result": result[0]})
    except Exception as e:
        return jsonify({"message": "Database connection failed", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
