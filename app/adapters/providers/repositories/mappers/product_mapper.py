from app.domain import Product


class ProductMapper:
    @staticmethod
    def to_domain(product_dict):
        return Product(oid=product_dict.get('_id'),
                       name=product_dict.get('name'),
                       amount=product_dict.get('amount'),
                       value=product_dict.get('value'),
                       expiration_date=product_dict.get('expirationDate'),
                       updated_at=product_dict.get('updatedAt'), )

    @staticmethod
    def from_domain(product):
        return {'_id': str(product.oid),
                'name': product.name,
                'amount': product.amount,
                'value': product.value,
                'expirationDate': product.expiration_date.isoformat(),
                'updatedAt': product.updated_at.isoformat()}
