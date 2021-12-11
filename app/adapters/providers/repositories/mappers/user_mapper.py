from app.domain import User


class UserMapper:
    @staticmethod
    def to_domain(user_dict):
        return User(oid=user_dict.get('oid'),
                    name=user_dict.get('name'),
                    created_at=user_dict.get('createdAt'))

    @staticmethod
    def from_domain(user):
        return {'oid': user.oid,
                'name': user.name,
                'createdAt': user.created_at.isoformat()}
