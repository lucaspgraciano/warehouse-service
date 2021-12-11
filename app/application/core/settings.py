import os

from dotenv import load_dotenv
from .logger import create_logger

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Settings:
    DEBUG = True
    PORT = int(os.getenv('PORT'))
    HOST = os.getenv('HOST')
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    DATABASE_URL = os.getenv('DATABASE_URL')

    def __init__(self):
        self.logger = create_logger(self.LOG_LEVEL)


settings = Settings()
