class InsertOneProductUsecase:
    def __init__(self, products_repository, datetime_utils):
        self.products_repository = products_repository
        self.datetime_utils = datetime_utils

    def execute(self, name, amount, value, expiration_date):
        return self.products_repository.insert_one(name=name,
                                                   amount=amount,
                                                   value=value,
                                                   expiration_date=self.datetime_utils.string_to_datetime(
                                                       expiration_date),
                                                   updated_at=self.datetime_utils.get_current_date())
