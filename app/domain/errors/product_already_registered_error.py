class ProductAlreadyRegisteredError(RuntimeError):
    """Raise when the product has already been registered"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'The {self.name} product has already been registered'

    @staticmethod
    def get_message():
        return 'PRODUCT_ALREADY_REGISTERED'
