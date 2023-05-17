"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi81c64dadc9vm2r8j0-a.oregon-postgres.render.com",
        database="todo_zvk9",
        user="root",
        password="xeDSStBBBzFH8Y5eDESL3Y7mJ17j37pR")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
