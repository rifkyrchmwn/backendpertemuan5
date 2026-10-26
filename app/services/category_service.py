from app.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def get_all_categories(self):
        categories = self.repo.get_all()
        return {"categories": categories, "total": len(categories)}, None

    def create_category(self, data):
        if not isinstance(data, dict):
            return None, {"body": "Body harus berupa JSON object yang valid"}

        errors = {}
        name = data.get("name")
        if not name or not isinstance(name, str) or not name.strip():
            errors["name"] = "Field name wajib diisi"

        if errors:
            return None, errors

        new_cat = self.repo.create(name.strip(), data.get("description", ""))
        return new_cat, None

    def get_products_by_category(self, category_id):
        category = self.repo.find_by_id(category_id)
        if not category:
            return None, {"category": "Kategori tidak ditemukan"}

        products = self.repo.get_products_by_category(category_id)
        return {
            "category_id": category_id,
            "products": products,
            "total": len(products)
        }, None