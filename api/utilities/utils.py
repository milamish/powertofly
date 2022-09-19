from functools import wraps
from typing import Callable, Any, Tuple

from flask import current_app as app
from flask_restful import abort

from werkzeug.exceptions import UnprocessableEntity


def format_error_response(message, data=None, meta=None, status=400):
    return {
        "data": data,
        "message": message,
        "meta": meta,
        "status": status
    }


def exception_handle(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, int]:
        try:
            return fn(*args, **kwargs)
        except UnprocessableEntity as error:
            error_msg = error.exc.messages['json']
            return abort(400, **format_error_response(error_msg))
        except Exception as exc:
            app.logger.error(exc)
            # Do db rollback if it was write request
            return abort(500, **format_error_response(str(exc)))

    return wrapper


error_schema = {
    "401": {
        "description": "Invalid Authentication token",
        "schema": {
            "properties": {
                "error": {
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "400": {
        "description": "Invalid data",
        "schema": {
            "properties": {
                "error": {
                    "type": "object",
                    "properties": {
                        "object_key": {
                            "type": "string"
                        }
                    },
                }
            },
            "type": "object"
        }
    }
}
