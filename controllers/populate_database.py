from models.database import Database

# Connexion à la base de données
db = Database()

# Ajout des catégories
categories = [
    ("Sacs à main",),
    ("Bijoux",),
    ("Accessoires pour cheveux",),
    ("Portefeuilles",),
]

db.execute_query("DELETE FROM categories")
db.execute_query("DELETE FROM products")

for category in categories:
    db.execute_query("INSERT INTO categories (name) VALUES (?)", category)

# Ajout des produits
products = [
    ("Sac en cuir noir", 10, 120.0, "Un sac élégant en cuir véritable", 1, "assets/images/sac_noir.jpg"),
    ("Bracelet en argent", 15, 50.0, "Un bracelet chic et intemporel", 2, "assets/images/bracelet_argent.jpg"),
    ("Serre-tête fleuri", 25, 15.0, "Un accessoire adorable pour toutes les occasions", 3, "assets/images/serre_tete.jpg"),
    ("Portefeuille en tissu", 8, 35.0, "Un portefeuille pratique et durable", 4, "assets/images/portefeuille.jpg"),
]

for product in products:
    db.execute_query("""
        INSERT INTO products (name, stock, price, description, category_id, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
    """, product)

print("Base de données remplie avec succès !")
