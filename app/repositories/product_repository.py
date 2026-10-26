from app.repositories.category_repository import mock_products

class ProductRepository:
    def get_all(self):
        return mock_products

    def find_by_id(self, product_id):
        return next((p for p in mock_products if p["id"] == product_id), None)

    def create(self, category_id, name, price):
        new_product = {
            "id": len(mock_products) + 101,
            "category_id": category_id,
            "name": name,
            "price": price
        }
        mock_products.append(new_product)
        return new_product

    def delete(self, product_id):
        global mock_products
        product = self.find_by_id(product_id)
        if product:
            mock_products[:] = [p for p in mock_products if p["id"] != product_id]
            return True
        return False