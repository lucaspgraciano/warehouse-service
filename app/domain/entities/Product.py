class Product:
    def __init__(self, oid, name, amount, value, expiration_date, updated_at):
        self.oid = oid
        self.name = name
        self.amount = amount
        self.value = value
        self.expiration_date = expiration_date
        self.updated_at = updated_at

    def __str__(self):
        return f' {{ name: {self.name} | amount: {self.amount} | value: {self.value} | expiration_date: {self.expiration_date} }}'
