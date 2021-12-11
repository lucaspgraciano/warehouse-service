from fastapi import FastAPI
from app.application import database, settings
from app.adapters import Router


def create_app():
    return FastAPI()


def run_app(app):
    database.connect()
    Router(app)
