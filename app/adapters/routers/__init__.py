from .product import api as product


class Router:
    def __init__(self, app):
        self.app = app
        self.app.include_router(router=product,
                                prefix='/product',
                                tags=['product'])
