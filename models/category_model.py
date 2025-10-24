import sqlite3

class CategoryModel:
    @staticmethod
    def get_all_categories():
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories

    @staticmethod
    def get_all_categories():
        conn = sqlite3.connect("db.sqlite")
        conn.row_factory = sqlite3.Row  # Permet de récupérer les résultats sous forme de dictionnaires
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        categories = cursor.fetchall()
        conn.close()
        return categories

    @staticmethod
    def add_category(name):
        # Connexion à la base de données
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()

        # Requête SQL pour ajouter une catégorie
        cursor.execute("""
            INSERT INTO categories (name)
            VALUES (?)
        """, (name,))

        # Validation et fermeture
        conn.commit()
        conn.close()


    @staticmethod
    def update_category(category_id, name):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (name, category_id))
        conn.commit()
        conn.close()


    @staticmethod
    def delete_category(category_id):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        conn.commit()
        conn.close()
