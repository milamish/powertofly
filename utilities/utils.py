from functools import wraps
from typing import Callable, Any, Tuple

from flask import current_app as app, current_app, g
from flask_restful import abort
from marshmallow import ValidationError as MarshmallowValidationError
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

'''
def get_app_package_name(package_name):
    with SqlAlchemySession() as session:
        repo = CopiaAndroidAppRepository(session)
        return repo.get_record_with_(package_name=package_name)


@pool
def get_or_create_access_token(cr, user_id):
    query = """
            select api_access_token.id, 
              api_access_token.user_id,  
              api_access_token.token,  
              res_company.id company_id,	 
              res_country.code country_code,  
              res_currency.name currency_name,  
              res_currency.symbol currency_symbol,  
              res_currency.position currency_position  
              from api_access_token    
              join res_company on api_access_token.company_id=res_company.id   
              join  res_partner on res_company.partner_id=res_partner.id   
              join res_country on res_partner.country_id=res_country.id  
              join res_currency on res_company.currency_id=res_currency.id 
              limit 1
          """
    cr.execute(query)
    return [dict(row) for row in cr.fetchall()]

'''
