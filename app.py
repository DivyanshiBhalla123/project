from distutils.log import debug
from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
    'id':tasks[-1]["id"]+1,
    'Name':request.json["Name"],
    'description':request.json.get("contact",""),
    'done':False
},
{
    'id':tasks[-1]["id"]+1,
    'Name':request.json["Name"],
    'description':request.json.get("contact",""),
    'done':False
}
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        },400)
    task={
        "id":tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }    
    tasks.append(task)
    return jsonify({
        "status":"success",
        "messsage":"task added"
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":tasks,

    })
if(__name__=="__main__"):
    app.run(debug=True)