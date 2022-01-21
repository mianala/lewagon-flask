from enum import unique
from wsgi import db

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.Text)

# product = Product()
# product.name = "Product rename"
# db.session.add(product)
# db.session.commit()