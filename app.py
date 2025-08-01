from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_controller = 1


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_controller
    data = request.get_json()
    new_task = Task(
        id=task_id_controller,
        title=data.get("title"),
        description=data.get("description"),
        completed=data.get("completed", False),
    )
    task_id_controller += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total": len(task_list),
    }

    return jsonify(output)


@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Tarefa não encontrada!"}), 404


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    for t in tasks:
        if t.id == id:
            t.title = data.get("title", t.title)
            t.description = data.get("description", t.description)
            t.completed = data.get("completed", t.completed)
            return jsonify({"message": "Tarefa atualizada com sucesso!"})

    return jsonify({"message": "Tarefa não encontrada!"}), 404


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t.id != id]
    return jsonify({"message": "Tarefa deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
