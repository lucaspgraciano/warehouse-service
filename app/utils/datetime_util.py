from datetime import datetime


class DatetimeUtils:
    @staticmethod
    def string_to_datetime(string):
        return datetime.strptime(string, '%d/%m/%Y')

    @staticmethod
    def get_current_date():
        return datetime.today()