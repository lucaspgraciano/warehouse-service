class User:
    def __init__(self, oid, name, created_at):
        self.oid = oid
        self.name = name
        self.created_at = created_at

    def __str__(self):
        return f'{{ name: {self.name} | created_at: {self.created_at} }}'
