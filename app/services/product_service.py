from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()
        self.category_repo = CategoryRepository()

    def get_all_products(self):
        products = self.product_repo.get_all()
        return {"products": products, "total": len(products)}, None

    def create_product(self, data):
        if not isinstance(data, dict):
            return None, {"body": "Body harus berupa JSON object yang valid"}

        errors = {}
        category_id = data.get("category_id")
        name = data.get("name")
        price = data.get("price")

        if not category_id or not self.category_repo.find_by_id(category_id):
            errors["category_id"] = "category_id tidak valid atau tidak ditemukan"
        if not name or not isinstance(name, str) or not name.strip():
            errors["name"] = "Field name wajib diisi"
        if price is None or not isinstance(price, (int, float)) or price <= 0:
            errors["price"] = "Field price harus berupa angka positif"

        if errors:
            return None, errors

        new_prod = self.product_repo.create(category_id, name.strip(), price)
        return new_prod, None

    def delete_product(self, product_id):
        product = self.product_repo.find_by_id(product_id)
        if not product:
            return False, {"product": "Produk tidak ditemukan"}

        self.product_repo.delete(product_id)
        return True, None