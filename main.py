from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# Function to connect to MySQL
def get_db():
    conn = mysql.connector.connect(
        host="localhost",      # your DB host
        user="root",           # your DB username
        password="Pavi@713", # your DB password
        database="healthbot"   # your DB name
    )
    return conn

# Home route
@app.get("/")
def home():
    return {"message": "FastAPI + MySQL working!"}

# Get all diseases
@app.get("/diseases")
def get_diseases():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM diseases")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"diseases": rows}

# Get info about one disease
@app.get("/disease/{name}")
def get_disease(name: str):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM diseases WHERE name = %s", (name,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return {"disease": row}
    else:
        return {"message": f"No data found for {name}"}