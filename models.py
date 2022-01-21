from enum import unique
from wsgi import dbm

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)