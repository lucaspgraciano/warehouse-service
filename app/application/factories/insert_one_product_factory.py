from app.application import database
from app.adapters.providers import ProductsRepository
from app.domain import FindByNameUsecase
from app.domain import InsertOneProductUsecase


class InsertOneProductFactory:
    @staticmethod
    def create():
        connection = database.connect()
        repository = ProductsRepository(product_entity=connection.db.products)
        find_by_name_usecase = FindByNameUsecase(products_repository=repository)
        usecase = InsertOneProductUsecase(products_repository=repository, find_by_name_usecase=find_by_name_usecase)
        return usecase
