import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Fetch environment variables (without default values)
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")

# Ensure all required environment variables are set
if not all([DB_HOST, DB_NAME, DB_USER, DB_PASS]):
    raise ValueError("Missing one or more required environment variables: DB_HOST, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD")

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST
        )
        return "Connected to PostgreSQL!", 200
    except Exception as e:
        return f"Database connection error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
