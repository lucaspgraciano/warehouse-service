from .mappers import ProductMapper


class ProductsRepository:
    def __init__(self, product_entity):
        self.Products = product_entity

    def insert_one(self, name, amount, value, expiration_date, updated_at):
        product_id = self.Products.insert_one({'name': name, 'amount': amount, 'value': value,
                                              'expirationDate': expiration_date, 'updatedAt': updated_at}).inserted_id
        return ProductMapper.to_domain({'oid': product_id, 'name': name, 'amount': amount, 'value': value,
                                        'expirationDate': expiration_date, 'updatedAt': updated_at})

    def find_all(self):
        products_dict = self.Products.find({'$query': {}, '$orderby': {'updatedAt': -1}})
        return list(map(lambda product: ProductMapper.to_domain(product), products_dict))
