# product_service/utils.py

# Import necessary modules and models
from .models import Product
from . import db

def create_product(name, description, price):
    """Create a new product."""
    new_product = Product(name=name, description=description, price=price)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product_id, name=None, description=None, price=None):
    """Update an existing product."""
    product = Product.query.get(product_id)
    if product:
        if name:
            product.name = name
        if description:
            product.description = description
        if price:
            product.price = price
        db.session.commit()
        return product
    else:
        return None

def delete_product(product_id):
    """Delete a product by its ID."""
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    else:
        return False
