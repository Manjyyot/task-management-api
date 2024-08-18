from flask import Flask, jsonify, request
app1 = Flask(__name__)

tasks = []

@app1.route("/deletetask/<Id>", methods=['DELETE'])
def deletetask(Id):
    for i in range(len(tasks)):
        if tasks[i]['id'] == int(Id):
            del tasks[i]
            return jsonify(" The task has been deleted")
        else:
           return jsonify("Invalid ID !") 
        
if __name__== '__main__':
    app1.run(debug=True)