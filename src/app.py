from flask import Flask
import pymysql
import os
 
app = Flask(__name__)
 
# RDS connection details (replace with your values or set as env vars)
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
 
@app.route('/')
def index():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users;")
        rows = cursor.fetchall()
        conn.close()
 
        result = "<h2>Users in RDS:</h2><ul>"
        for row in rows:
            result += f"<li>{row[1]} - {row[2]}</li>"
        result += "</ul>"
        return result
 
    except Exception as e:
        return f"Error: {str(e)}"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


