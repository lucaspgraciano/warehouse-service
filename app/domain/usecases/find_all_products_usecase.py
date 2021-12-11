class FindAllProductsUsecase:
    def __init__(self, products_repository):
        self.products_repository = products_repository

    def execute(self):
        return self.products_repository.find_all()
