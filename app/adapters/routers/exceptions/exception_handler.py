from fastapi import Request
from app.domain import ProductAlreadyRegisteredError
from fastapi.responses import JSONResponse


class ExceptionHandler:
    def __init__(self, app):
        @app.exception_handler(ProductAlreadyRegisteredError)
        def product_already_registered_error(request: Request, error: ProductAlreadyRegisteredError):
            return JSONResponse(status_code=400, content={'message': error.get_message()})
