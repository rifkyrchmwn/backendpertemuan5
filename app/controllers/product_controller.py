from flask import request
from app.services.product_service import ProductService
from app.utils.response_helper import success_response, fail_response

class ProductController:
    def __init__(self):
        self.service = ProductService()

    def get_products(self):
        data, _ = self.service.get_all_products()
        return success_response(data=data)

    def create_product(self):
        if not request.is_json:
            return fail_response({"content_type": "Header Harus application/json"}, 400)

        body = request.get_json(silent=True)
        data, errors = self.service.create_product(body)
        if errors:
            return fail_response(errors, 400)

        return success_response(data=data, message="Produk berhasil ditambahkan", code=201)

    def delete_product(self, product_id):
        success, errors = self.service.delete_product(product_id)
        if errors:
            return fail_response(errors, 404)

        return success_response(message="Produk berhasil dihapus", code=200)