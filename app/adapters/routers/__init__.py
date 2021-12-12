from .product import api as product
from .exceptions import ExceptionHandler


class Router:
    def __init__(self, app):
        app.include_router(router=product,
                           prefix='/product',
                           tags=['product'])
        ExceptionHandler(app)
