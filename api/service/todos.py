import sys

from flask import jsonify, request, current_app, abort
from api.models.todo import ToDo
from werkzeug.exceptions import NotFound
from api.utils.response import NotFoundException, InternalServerError

def get_all_todos() :
    try :
        todos = ToDo.query.all()
        current_app.logger.info("load data from database successfull")
        return jsonify(
                status=200,
                message="success",
                data=[todo.serialize() for todo in todos]
            ), 200

    except Exception as e:
        return InternalServerError(e)

def get_todos_by_id(id_) :
    try :
        todo = ToDo.query.filter_by(id=id_).first()
        if not todo :
            raise NotFound("to do not found")
        current_app.logger.info("load data from database successfull")
        return jsonify(
                status=200,
                message="success",
                data=todo.serialize()
            ), 200

    except NotFound as e :
        return NotFoundException(e)
    except Exception as e:
        return InternalServerError(e)

def create_todo() :
    name = request.json["name"]
    description = request.json["description"]
    try :

        todo = ToDo(
            name=name,
            description=description
        )
        todo.save()
        current_app.logger.info("save db successfull")

        return jsonify(
            status=201,
            message="success creating todos",
            data=todo.serialize()
        ), 201

    except Exception as e:
        return InternalServerError(e)


