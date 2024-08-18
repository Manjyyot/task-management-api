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


@app1.route("/updatetask/<Id>", methods=['PUT'])
def updatetask(Id):
    for task in tasks:
        if task['id'] == int(Id):
            updated_task = request.json
            task.update(updated_task)
            return jsonify(" The new tasks has been updated")
        else:
            return jsonify("Invalid ID")

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