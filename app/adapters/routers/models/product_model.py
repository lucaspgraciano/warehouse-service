from pydantic import BaseModel


class ProductModel(BaseModel):
    name: str
    amount: int
    value: float
    expirationDate: str
