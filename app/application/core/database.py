import logging

from pymongo import MongoClient
from .settings import settings


class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.connected = False
        self.settings = settings

    def connect(self):
        if self.connected is False:
            logging.info('Starting connection to database.')
            self.client = MongoClient(self.settings.DATABASE_URL)
            self.db = self.client.warehouse
            self.connected = True
            logging.info('Database connected.')
        return self

    def close(self):
        logging.info('Closing connection to database.')
        self.client.close()
        logging.info('Database disconnected.')


database = Database()
