from flask import jsonify, current_app


def InternalServerError(e) :
    current_app.logger.error(e)
    return jsonify(
            status=500,
            message="internal server error"
    ), 500

def NotFoundException(e) :
    current_app.logger.error(e)
    return jsonify(
        status=404,
        message="internal server error"
    ), 404