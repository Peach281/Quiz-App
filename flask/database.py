from flask import Flask,request,jsonify
from flask_cors import CORS
import sqlite3
import hashlib
app = Flask(__name__)
CORS(app)
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
import sqlite3

DATABASE = "data.db"



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
        hashed_password=hashlib.sha256(password.encode()).hexdigest()
        db=get_db()
        cursor=db.cursor()
        cursor.execute('INSERT INTO users (username,email,password) VALUES (?,?,?)',(name,email,hashed_password))
        db.commit()
        db.close()
        return {'message':'Data Submitted Successfully'},200
    except Exception as  e:
        return {'error':str(e)},500
@app.route('/login',methods=['POST'])
def login():
    req=request.get_json()
    username = req.get('username')
    password = req.get('password')
    if not username or not password:
        return {'error':'Please enter the username and password'},400
    try:
        db=get_db()
        cursor=db.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?',(username,))
        user=cursor.fetchone()
        db.close()
        if user:
            hashed_password=hashlib.sha256(password.encode()).hexdigest()
            if(hashed_password==user['password']):
                return {'id':user['id'],'message':'Login successful'},200
        return {'error':'Invalid username or password'},401
    except Exception as e:
        return {'error':str(e)},500
@app.route('/admin',methods=['POST'])
def admin():
    data=request.get_json()
    id=data.get('id')
    if(id==2):
        return {'message':'You are admin'}
    
        

if __name__=='__main__':
    app.run(debug=True)