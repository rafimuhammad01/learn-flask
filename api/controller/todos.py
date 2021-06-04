from flask import Blueprint
from api.service.todos import get_all_todos, create_todo, get_todos_by_id

todos = Blueprint("todos", __name__)

todos.route("/", methods=["GET"])(get_all_todos)
todos.route("/", methods=["POST"])(create_todo)
todos.route("/<id_>", methods=["GET"])(get_todos_by_id)