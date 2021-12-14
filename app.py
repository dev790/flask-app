from logging import error
from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        'id':1,
        'contact':u'9004115835',
        'name':u'Dev',
        'done':False

    },
    {
        'id':2,
        'contact':u'9892931665',
        'name':u'zampa',
        'done':False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    task={
        'id': tasks[-1]['id']+1,
        'contact':request.json['contact'],
        'name':request.json.get('name',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added succesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)