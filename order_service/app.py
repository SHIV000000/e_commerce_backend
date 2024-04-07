# order_service/app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Shiv0518:Shiv0518@localhost/ecommerce_db'
db = SQLAlchemy(app)

# Define the Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    status = db.Column(db.String(50))

    def __init__(self, user_id, product_id, quantity, status):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    status = data.get('status', 'Pending')  # Default status is 'Pending'

    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity, status=status)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order created successfully"}), 201

# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = []
    for order in orders:
        order_data = {
            'id': order.id,
            'user_id': order.user_id,
            'product_id': order.product_id,
            'quantity': order.quantity,
            'status': order.status
        }
        result.append(order_data)
    return jsonify(result), 200

# Endpoint to get a specific order by ID
@app.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order_data = {
        'id': order.id,
        'user_id': order.user_id,
        'product_id': order.product_id,
        'quantity': order.quantity,
        'status': order.status
    }
    return jsonify(order_data), 200

if __name__ == '__main__':
    app.run(debug=True)
