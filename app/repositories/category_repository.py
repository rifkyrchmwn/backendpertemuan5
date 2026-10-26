mock_categories = [
    {"id": 1, "name": "Electronics", "description": "Gadgets and devices"},
    {"id": 2, "name": "Books", "description": "Educational and literature"},
    {"id": 3, "name": "Accessories", "description": "Computer and phone accessories"}
]

mock_products = [
    # Kategori 1: Electronics (3 Produk)
    {"id": 101, "category_id": 1, "name": "Laptop Gaming", "price": 15000000},
    {"id": 102, "category_id": 1, "name": "Smartphone", "price": 5000000},
    {"id": 103, "category_id": 1, "name": "Monitor 24 Inch 144Hz", "price": 2500000},

    # Kategori 2: Books (3 Produk)
    {"id": 104, "category_id": 2, "name": "Pemrograman Python Dasar", "price": 95000},
    {"id": 105, "category_id": 2, "name": "Desain RESTful API Modern", "price": 120000},
    {"id": 106, "category_id": 2, "name": "Struktur Data & Algoritma", "price": 110000},

    # Kategori 3: Accessories (2 Produk)
    {"id": 107, "category_id": 3, "name": "Mouse Gaming Wireless", "price": 350000},
    {"id": 108, "category_id": 3, "name": "Keyboard Mechanical RGB", "price": 750000}
]

class CategoryRepository:
    def get_all(self):
        return mock_categories

    def find_by_id(self, category_id):
        return next((c for c in mock_categories if c["id"] == category_id), None)

    def create(self, name, description):
        new_category = {
            "id": len(mock_categories) + 1,
            "name": name,
            "description": description
        }
        mock_categories.append(new_category)
        return new_category

    def get_products_by_category(self, category_id):
        return [p for p in mock_products if p["category_id"] == category_id]