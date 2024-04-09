from flask import Flask,request,jsonify
from flask_cors import CORS
import sqlite3
import hashlib
from Questions import questions

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
            password TEXT NOT NULL,
            total_score INTEGER DEFAULT 0
        )
    ''')
    db.commit()
    db.close()
def create_ques():
    db1=get_db()
    cursor=db1.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ques(
        id TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        genre TEXT NOT NULL,
        ques TEXT PRIMARY KEY NOT NULL,
        options TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')
    db1.commit()
    db1.close()



def get_db():
    db=sqlite3.connect(DATABASE)
    db.row_factory=sqlite3.Row
    return db
create_table()
create_ques()

def Ques():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT ques FROM Ques")
    prev_questions = cursor.fetchall()
    for ques in questions:
        if ques['name'] not in [row[0] for row in prev_questions]:
            cursor.execute('''INSERT OR REPLACE INTO Ques (genre,ques,options,answer) VALUES(?,?,?,?)''',
                           (ques["genre"],ques["name"], ",".join(ques["options"]), ques["answer"]))
    db.commit()
    db.close()



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
    if(id==3):
        return jsonify({'message':'You are admin'})
    else:
        return jsonify({'message':'You are not the admin'}),401
@app.route('/Data',methods=['GET'])
def Data():
    genre = request.args.get('genre')
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM Ques WHERE genre=?', (genre,))
    rows = cursor.fetchall()
    db.close()
    return jsonify([dict(row) for row in rows])

@app.route('/addQues',methods=['POST'])
def addQues():
    try:
        data=request.get_json()
        genre = data.get("genre")
        print(genre)
        name=data.get("name")
        options = data.get("options")
        answer = data.get("answer")

        db = get_db()
        cursor = db.cursor()
        cursor.execute('INSERT INTO Ques (genre, ques, options, answer) VALUES (?, ?, ?, ?)',
                        (genre, name, options, answer))
        db.commit()
        db.close()

        return jsonify({'message': 'Question added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/dlt",methods = ['POST'])
def delete():
    try:
        data=request.get_json()
        name = data.get("name")
        db=get_db()
        cursor=db.cursor()
        cursor.execute('DELETE FROM Ques WHERE ques=?',(name,))
        db.commit()
        db.close()
        return jsonify({'message':'Question deleted successfully'}),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@app.route("/change",methods=['POST'])
def change():
    data=request.get_json()
    name=data.get("name")
    answer=data.get("answer")
    db=get_db()
    cursor=db.cursor()
    cursor.execute('SELECT * FROM Ques WHERE ques=?',(name,))
    row=cursor.fetchone()
    print(row)
    try:
        cursor.execute('UPDATE Ques SET answer=? WHERE ques=?', ( answer, name,))
        db.commit()
        db.close()
        return jsonify({'message': 'done'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route("/getPoints",methods=['POST'])
def getPoints():
    data=request.get_json()
    username = data.get('username')
    new_score = data.get('total')
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT total_score FROM users WHERE id = ?', (username))
        current_total_score = cursor.fetchone()['total_score']
        updated_total_score = current_total_score + new_score
        cursor.execute('UPDATE users SET total_score = ? WHERE id = ?', (updated_total_score, username))
        db.commit()
        db.close()
        return jsonify({'message': 'Score updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__=='__main__':
    app.run(debug=True)

