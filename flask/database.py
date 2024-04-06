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
            password TEXT NOT NULL,
            total_score INTEGER DEFAULT 0
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
    
        
@app.route('/SportsData',methods=['GET'])
def ques():
    questions=[
        {
            "id":1,
            "name":"Who won the 10th Italian Open title in 2021?",
            "options":['Novack Djokovic','Rafael Nadal','Dominic Thiem','Stefanos Tsitsipas'],
            "answer":"Rafael Nadal"
        },
        {
            "id":2,
            "name":"Only three countries have won the Women's Rugby World Cup- New Zealand, England, and who?",
            "options":['USA', 'Argentina' ,'Romania','Georgia'],
            "answer":"USA"
        }
        ,
        {
            "id":3,
            "name": "In cricket which of the following fielding positions is behind the batsman?",
            "options":['Mid-wicket','First slip','Cover','Mid-off'],
            "answer":"First slip"
        },
        {
            "id":4,
            "name":" The term 'Dolphin Kick' is associated with which of the following games?",
            "options":['Badminton','Squash','Swimming','Golf'],
            "answer":"Swimming"
        },
        {
            "id":5,
            "name":"Which boxer fought against Muhammad Ali and won?",
            "options":['Joe Frazier','Tony Esperti', 'Jim Robinson', 'Donnie Fleeman' ],
            "answer":'Joe Frazier'
        }
        
    ]
    
    return jsonify(questions)
@app.route('/LiteratureData',methods=['GET'])
def LitData():
    q=[
    {
        "id":1,
        "name":"Who was the author of the famous storybook 'Alice's Adventures in Wonderland'?",
        "options":["Rudyard Kipling","John Keats","Lewis Carroll","H G Wells"],
        "answer":"Lewis Carroll"
    },
    {
        "id":2,
        "name":"Name the book which opens with the line 'All children, except one grew up'?",
        "options":[" The Railway Children","Winnie The Poo","Jungle Book","Peter Pan"],
        "answer":"Peter Pan"
    },
    {
        "id":3,
        "name":"Name the book which opens with the line 'All children, except one grew up'?",
        "options":[" The Railway Children","Winnie The Poo","Jungle Book","Peter Pan"],
        "answer":"Peter Pan"
    },
    {
        "id":4,
        "name":"What author became famous for his six-volume biography of Lincoln?",
        "options":["Mark Twain","Ruskin Bond","Carl Sandburg","HP Lovecraft"],
        "answer":"Carl Sandburg"
    },
    {
        "id":5,
        "name":"What did Sherlock Holmes do after retiring from his detective practice?",
        "options":["Doctor","Musician","Bee Keeper","Chef"],
        "answer":"Bee Keeper"
    },
    {
        "id":6,
        "name":"What traveler compiled a widely read book about his travels?",
        "options":["Christoher Columbus","Marco Polo","Ferdinand Magellan","Ponce De Leon"],
        "answer":"Marco Polo"
    },
    {
        "id":7,
        "name":"Which is the first Harry Potter book?",
        "options":["HP and the Goblet of Fire","HP and the Philosopher's Stone","HP and the Chamber of Secrets","HP and the God of small Things"],
        "answer":"HP and the Philosopher's Stone"
    },
    {
        "id":8,
        "name":"What was the nationality of Robert Louis Stevenson, writer of 'Treasure Island'?",
        "options":["Scottish","Irish","Canadian","Japanese"],
        "answer":"Scottish"
    },
    ]
    return jsonify(q)

@app.route('/PoliticsData',methods=['GET'])
def Politics():
    ques=[
        {
            "id":1,
            "name":"Who has the right to form a new state or change the boundary?",
            "options":['Cabinet','Parliament','Prime Minister','President'],
            "answer":"Parliament"
        },
        {
            "id":2,
            "name":"Who was the first Vice President of India?",
            "options":['Dr. Zakir Hussain','Gopal Swaroop Pathak','Dr. S. Radhakrishnan','None of the above'],
            "answer":"Dr. S. Radhakrishnan"
        },
        {
            "id":3,
            "name":"Good Friday Agreement signed in 1998 was aimed to end violence in which country?",
            "options":['Philippines','Chile','Northern Ireland','Russia'],
            "answer":"Northern Ireland"
        },
        {
            "id":4,
            "name":"'Washington Declaration' is a bilateral agreement that was signed between the US and which country?",
            "options":['Philippines','South Korea','Canada','UK'],
            "answer":"South Korea"
        },
        {
            "id":5,
            "name":"'Legal Debt Ceiling' is associated with which country?",
            "options":['USA','Japan','India','UK'],
            "answer":"USA"
        },
        {
            "id":6,
            "name":"Ministry of External Affairs along with its counterpart of which country launched a foundation to promote dialogue between youth leaders?",
            "options":['USA','Japan','France','UK'],
            "answer":"France"
        },
        {
            "id":7,
            "name":"Sitiveni Rabuka, who apologised for his role in 1987 military coup, is the Prime Minister of which country?",
            "options":['Myanmar','Thailand','South Africa','Fiji'],
            "answer":"Fiji"
        },
        {
            "id":8,
            "name":"Which country has recently commissioned the Dangote Refinery?",
            "options":['Russia','France','Nigeria','Sri Lanka'],
            "answer":"Nigeria"
        }
    ]
    return jsonify(ques)
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

