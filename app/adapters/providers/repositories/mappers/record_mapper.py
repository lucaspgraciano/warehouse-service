from app.domain import Record


class RecordMapper:
    @staticmethod
    def to_domain(record_dict):
        return Record(oid=record_dict.get('_id'),
                      type=record_dict.get('type'),
                      product_name=record_dict.get('productName'),
                      amount=record_dict.get('amount'),
                      user=record_dict.get('user'),
                      date=record_dict.get('date'))

    @staticmethod
    def from_domain(record):
        return {'oid': record.oid,
                'type': record.type,
                'productName': record.product_name,
                'amount': record.amount,
                'user': record.user,
                'date': record.date.isoformat()}
