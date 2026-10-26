from flask import request
from app.services.category_service import CategoryService
from app.utils.response_helper import success_response, fail_response

class CategoryController:
    def __init__(self):
        self.service = CategoryService()

    def get_categories(self):
        data, _ = self.service.get_all_categories()
        return success_response(data=data)

    def create_category(self):
        if not request.is_json:
            return fail_response({"content_type": "Header Harus application/json"}, 400)

        body = request.get_json(silent=True)
        data, errors = self.service.create_category(body)
        if errors:
            return fail_response(errors, 400)

        return success_response(data=data, message="Kategori berhasil ditambahkan", code=201)

    def get_category_products(self, category_id):
        data, errors = self.service.get_products_by_category(category_id)
        if errors:
            return fail_response(errors, 404)

        return success_response(data=data)