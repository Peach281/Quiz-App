from flask import Flask,request,jsonify
from flask_cors import CORS
import sqlite3
app = Flask(__name__)
CORS(app, resources={r"/register": {"origins": "http://localhost:5173"}})
DATABASE = "data.db"
def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    db.commit()
    db.close()

def get_db():
    db=sqlite3.connect(DATABASE)
    db.row_factory=sqlite3.Row
    return db
create_table()
@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password :
        return jsonify({'error':'Name and email are required'}),400
    try:
        db=get_db()
        cursor=db.cursor()
        cursor.execute('INSERT INTO users (username,email,password) VALUES (?,?,?)',(name,email,password))
        db.commit()
        db.close()
        return jsonify({'message':'Data Submitted Successfully'}),200
    except Exception as  e:
        return jsonify({'error':str(e)}),500
if __name__=='__main__':
    app.run(debug=True)