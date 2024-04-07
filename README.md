# E-commerce Microservices Backend

This project is a backend system for an e-commerce platform, consisting of multiple microservices built using Flask and SQLAlchemy. It includes microservices for user authentication (`auth_service`), order management (`order_service`), and product management (`product_service`).

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/SHIV000000/e_commerce_backend.git
```

## Install dependencies:

```bash
cd e_commerce_backend
pip install -r requirements.txt
```

## Configuration
### Set up the PostgreSQL database:

```bash
Install PostgreSQL and create a database for each microservice.
Update the database URIs in the config.py files of each microservice (e.g., auth_service/config.py, order_service/config.py, product_service/config.py).
```

## Set up environment variables:

Create a .env file in the root directory.
Add environment variables for secret keys, database URIs, etc. For example:
```bash
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/ecommerce_db
```
## Usage
Run each microservice:

```bash
cd auth_service
python app.py

cd order_service
python app.py

cd product_service
python app.py
```

Access the APIs at the following endpoints:

Authentication Service: http://localhost:5000
Order Service: http://localhost:5001
Product Service: http://localhost:5002

## Testing
Run tests for each microservice:

```bash
cd auth_service/tests
python -m unittest discover -s . -p 'test_*.py'
```
```bash
cd order_service/tests
python -m unittest discover -s . -p 'test_*.py'
```
```bash
cd product_service/tests
python -m unittest discover -s . -p 'test_*.py'
```
    
