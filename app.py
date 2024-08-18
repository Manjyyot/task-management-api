from flask import Flask, jsonify, request
app1 = Flask(__name__)

tasks = []
@app1.route("/tasks", methods=['GET'])
def getAllTasks():
    return jsonify(tasks)


@app1.route("/tasks/<Id>", methods=['GET'])
def getProductById(Id):
    for task in tasks:
        if (task['id'] == int(Id)):
            return jsonify(task) 

@app1.route("/addtask", methods=['POST'])
def addtasks():
    # request and response
    task = request.json
    tasks.append(task)
    return jsonify(" The new tasks has been added")


if __name__== '__main__':
    app1.run(debug=True)