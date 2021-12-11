from app.application import database
from app.adapters.providers import ProductsRepository
from app.domain import FindAllProductsUsecase


class FindAllProductsFactory:
    @staticmethod
    def create():
        connection = database.connect()
        repository = ProductsRepository(product_entity=connection.db.products)
        usecase = FindAllProductsUsecase(products_repository=repository)
        return usecase
