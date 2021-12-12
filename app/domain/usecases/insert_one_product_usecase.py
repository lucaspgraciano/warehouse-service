from app.utils import DatetimeUtils, TextUtil
from app.domain import ProductAlreadyRegisteredError


class InsertOneProductUsecase:
    def __init__(self, products_repository, find_by_name_usecase):
        self.products_repository = products_repository
        self.find_by_name_usecase = find_by_name_usecase

    def execute(self, name, amount, value, expiration_date):
        self.__check_if_product_already_registered(TextUtil.slugify_text(name))
        return self.products_repository.insert_one(name=TextUtil.slugify_text(name),
                                                   amount=amount,
                                                   value=value,
                                                   expiration_date=DatetimeUtils.string_to_datetime(expiration_date),
                                                   updated_at=DatetimeUtils.get_current_date())

    def __check_if_product_already_registered(self, name):
        if self.find_by_name_usecase.execute(name=name) is not None:
            raise ProductAlreadyRegisteredError(name=name)
