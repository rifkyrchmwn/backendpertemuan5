from flask import Blueprint
from app.controllers.product_controller import ProductController

product_bp_v1 = Blueprint('product_v1', __name__, url_prefix='/api/v1/products')
controller = ProductController()

@product_bp_v1.route('', methods=['GET'])
def get_products():
    return controller.get_products()

@product_bp_v1.route('', methods=['POST'])
def create_product():
    return controller.create_product()

@product_bp_v1.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return controller.delete_product(product_id)