from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.adapters.providers import ProductMapper
from app.application.factories import FindAllProductsFactory, InsertOneProductFactory

api = APIRouter()

find_all_products_usecase = FindAllProductsFactory.create()
insert_one_product_usecase = InsertOneProductFactory.create()


class ProductModel(BaseModel):
    name: str
    amount: int
    value: float
    expirationDate: str


@api.get('/')
def get_product():
    products = find_all_products_usecase.execute()
    return [ProductMapper.from_domain(product) for product in products], HTTPException(200)


@api.post('')
def post_product(data: ProductModel):
    inserted_product = insert_one_product_usecase.execute(name=data.name,
                                                          amount=data.amount,
                                                          value=data.value,
                                                          expiration_date=data.expirationDate)
    return ProductMapper.from_domain(inserted_product), HTTPException(200)
