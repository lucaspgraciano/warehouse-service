class Record:
    def __init__(self, oid, type, product_name, amount, user, date):
        self.oid = oid
        self.type = type
        self.product_name = product_name
        self.amount = amount
        self.user = user
        self.date = date

    def __str__(self):
        return f'{{ type: {self.type} | product: {self.product_name} | amount: {self.amount} | user: {self.user} | date: {self.date} }}'
