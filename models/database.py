import sqlite3

class Database:
    def __init__(self, db_name="stock_management.db"):
        # Connexion à la base de données SQLite (check_same_thread=False si multithreading nécessaire)
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        # Crée les tables si elles n'existent pas déjà
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                stock INTEGER NOT NULL,
                price REAL NOT NULL,
                description TEXT,
                category_id INTEGER,
                image_path TEXT,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        """)
        self.conn.commit()

    def execute_query(self, query, params=None):
        """
        Exécute une requête SQL avec ou sans paramètres.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params or ())
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erreur SQLite: {e}")
            raise

    def fetch_one(self, query, params=None):
        """
        Exécute une requête SQL et retourne un seul résultat.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchone()

    def fetch_all(self, query, params=None):
        """
        Exécute une requête SQL et retourne tous les résultats.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()

    def close_connection(self):
        """
        Ferme la connexion à la base de données.
        """
        self.conn.close()

    def insert_product(self, name, stock, price, description=None, category_id=None, image_path=None):
        """
        Méthode pour insérer un produit dans la base de données.
        """
        query = """
        INSERT INTO products (name, stock, price, description, category_id, image_path)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.execute_query(query, (name, stock, price, description, category_id, image_path))

    def insert_user(self, username, password):
        """
        Méthode pour insérer un utilisateur dans la base de données.
        """
        query = """
        INSERT INTO users (username, password)
        VALUES (?, ?)
        """
        self.execute_query(query, (username, password))

    def insert_category(self, name):
        """
        Méthode pour insérer une catégorie dans la base de données.
        """
        query = """
        INSERT INTO categories (name)
        VALUES (?)
        """
        self.execute_query(query, (name,))
