from models.category_model import CategoryModel

class CategoryController:
    def get_categories(self):
        return CategoryModel.get_all_categories()

    def get_category_by_id(self, category_id):
        return CategoryModel.get_category_by_id(category_id)

    def add_category(self, name):
        # Utilisez CategoryModel pour ajouter une catégorie
        CategoryModel.add_category(name)

    def update_category(self, category_id, name):
        CategoryModel.update_category(category_id, name)

    def delete_category(self, category_id):
        CategoryModel.delete_category(category_id)
