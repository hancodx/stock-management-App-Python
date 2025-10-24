# models/product_model.py

import sqlite3

class ProductModel:
    
    @staticmethod
    def get_all_products():
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, stock, image_path FROM products")
        products = cursor.fetchall()
        conn.close()
        return products

    @staticmethod
    def get_product_by_id(product_id):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, stock, image_path FROM products WHERE id = ?", (product_id,))
        product = cursor.fetchone()  # Fetch a single product by ID
        conn.close()
        return product

    @staticmethod
    def add_product(name, price, stock, image_path):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO products (name, price, stock, image_path)
                          VALUES (?, ?, ?, ?)""", (name, price, stock, image_path))
        conn.commit()
        conn.close()

    @staticmethod
    def update_product(product_id, name, price, stock, image_path):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("""UPDATE products SET name = ?, price = ?, stock = ?, image_path = ? WHERE id = ?""", 
                       (name, price, stock, image_path, product_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_product(product_id):
        conn = sqlite3.connect("db.sqlite")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()
