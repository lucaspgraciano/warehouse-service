class FindByNameUsecase:
    def __init__(self, products_repository):
        self.products_repository = products_repository

    def execute(self, name):
        return self.products_repository.find_by_name(name=name)
