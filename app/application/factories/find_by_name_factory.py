from app.application import database
from app.adapters.providers import ProductsRepository
from app.domain import FindByNameUsecase


class FindByNameFactory:
    @staticmethod
    def create():
        connection = database.connect()
        repository = ProductsRepository(product_entity=connection.db.products)
        usecase = FindByNameUsecase()
        return usecase