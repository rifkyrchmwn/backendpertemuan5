from flask import Blueprint
from app.controllers.category_controller import CategoryController

category_bp_v1 = Blueprint('category_v1', __name__, url_prefix='/api/v1/categories')
controller = CategoryController()

@category_bp_v1.route('', methods=['GET'])
def get_categories():
    return controller.get_categories()

@category_bp_v1.route('', methods=['POST'])
def create_category():
    return controller.create_category()

@category_bp_v1.route('/<int:category_id>/products', methods=['GET'])
def get_category_products(category_id):
    return controller.get_category_products(category_id)