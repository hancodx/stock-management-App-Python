# controllers/product_controller.py
from models.product_model import ProductModel

class ProductController:
    def get_products(self):
        return ProductModel.get_all_products()

    def add_product(self, name, price, stock, image_path):
        ProductModel.add_product(name, price, stock, image_path)

    def update_product(self, product_id, name, price, stock, image_path):
        ProductModel.update_product(product_id, name, price, stock, image_path)

    def delete_product(self, product_id):
        ProductModel.delete_product(product_id)

    def show_add_product_form(self):
        # Récupérer toutes les catégories
        categories = CategoryModel.get_all_categories()
        return render_template('products/add-product.html', categories=categories)


