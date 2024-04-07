# product_service/app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the database URI for the product service
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Shiv0518:Shiv0518@localhost/ecommerce_db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)

# Route for creating a new product
@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if not name or not price:
        return jsonify({"error": "Missing required fields"}), 400

    new_product = Product(name=name, price=price, description=description)
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"}), 201

# Route for getting all products
@app.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }
        product_list.append(product_data)

    return jsonify({"products": product_list}), 200

# Route for getting a specific product by ID
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    product_data = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "description": product.description
    }

    return jsonify(product_data), 200

# Route for updating a product by ID
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')

    if name:
        product.name = name
    if price:
        product.price = price
    if description:
        product.description = description

    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200

# Route for deleting a product by ID
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
