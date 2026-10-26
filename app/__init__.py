from flask import Flask
from app.routes.v1.category_routes import category_bp_v1
from app.routes.v1.product_routes import product_bp_v1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(category_bp_v1)
    app.register_blueprint(product_bp_v1)
    return app