# models/product_model.py
class ProductModel:
    def __init__(self, name, stock, price, description=None, category_id=None, image_path=None):
        self.name = name
        self.stock = stock
        self.price = price
        self.description = description
        self.category_id = category_id
        self.image_path = image_path

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"
