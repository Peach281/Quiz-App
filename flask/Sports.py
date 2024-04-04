from flask import Flask,request,jsonify
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
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
            "answer":"Badminton"
        },
        {
            "id":5,
            "name":"Which boxer fought against Muhammad Ali and won?",
            "options":['Joe Frazier','Tony Esperti', 'Jim Robinson', 'Donnie Fleeman' ],
            "answer":'Joe Frazier'
        }
        
    ]
    sorted_ques=sorted(questions,key=lambda x:x['id'])
    return jsonify(sorted_ques)
if __name__=='__main__':
    app.run(debug=True)
