import os

from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Settings:
    DEBUG = True
    PORT = int(os.getenv('PORT'))
    HOST = os.getenv('HOST')
    DATABASE_URL = os.getenv('DATABASE_URL')


settings = Settings()
