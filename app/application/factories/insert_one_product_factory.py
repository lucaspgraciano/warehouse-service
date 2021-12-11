from app.application import database
from app.adapters.providers import ProductsRepository
from app.utils import DatetimeUtils
from app.domain import InsertOneProductUsecase


class InsertOneProductFactory:
    @staticmethod
    def create():
        connection = database.connect()
        repository = ProductsRepository(product_entity=connection.db.products)
        datetime_utils = DatetimeUtils
        usecase = InsertOneProductUsecase(products_repository=repository,
                                          datetime_utils=datetime_utils)
        return usecase
