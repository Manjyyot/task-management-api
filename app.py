from flask import Flask, jsonify, request
app1 = Flask(__name__)

tasks = [{"id": 1, "title": "Laptop", "description": "Ascer laptop", "status": "Sold","created_at": "12-Aug", "updated_at": "14-aug"}, 
{"id": 2, "title": "Mobile", "description": "IPHONE", "status": "Available","created_at": "13-Aug", "updated_at": "15-aug"}]
# tasks = []

@app1.route("/updatetask/<Id>", methods=['PUT'])
def updatetask(Id):
    for task in tasks:
        if task['id'] == int(Id):
            updated_task = request.json
            task.update(updated_task)
            return jsonify(" The new tasks has been updated")
        else:
            return jsonify("Invalid ID")

if __name__== '__main__':
    app1.run(debug=True)