# Stock Management App – Python (MTI Project)

A **desktop stock management application** built with **Python**, **SQLite3**, and an **MVC architecture**.  
This project was developed as part of the **MTI (Méthodes et Techniques Informatiques)** module to demonstrate object-oriented programming **OOP**, database integration, and the use of **software design patterns**.

---

## - Overview
The **Stock Management App** allows users to manage inventory easily through a graphical interface.  
It supports authentication, product and category management, and database persistence — all structured using a clean MVC architecture.

---

## - Key Features
✅ User authentication (login/register)  
✅ Manage product categories  
✅ Add, edit, delete, and view products  
✅ Automatically populate the database with initial data  
✅ Store product images and descriptions  
✅ SQLite database for local persistence  
✅ Clean, modular MVC structure (Models, Views, Controllers)

---

## - Architecture & Design Patterns

The project follows an **MVC (Model–View–Controller)** architecture.

| Layer | Description |
|-------|--------------|
| **Model** | Handles data access and manipulation (database operations using SQLite). |
| **View** | Represents the user interface (Tkinter or templates if GUI/web version). |
| **Controller** | Acts as a bridge between models and views, containing the business logic. |

### - Controllers
Each controller manages a specific part of the application:
- **`auth_controller.py`** – Manages user authentication (login, register).  
- **`category_controller.py`** – Handles CRUD operations for product categories.  
- **`product_controller.py`** – Manages product operations (add, update, delete, list).  
- **`user_controller.py`** – Handles user-related logic.  
- **`populate_database.py`** – Seeds the database with default categories and products.

---

## - Database Design

The database uses **SQLite3** and is automatically created as `stock_management.db` in the root directory.

### Main Tables
#### `users`
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| username | TEXT | Unique username |
| password | TEXT | Hashed user password |

#### `categories`
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | TEXT | Category name |

#### `products`
| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | TEXT | Product name |
| stock | INTEGER | Quantity available |
| price | REAL | Product price |
| description | TEXT | Product description |
| category_id | INTEGER | Foreign key → `categories.id` |
| image_path | TEXT | Path to product image |

---

## - Example Database Content
The `populate_database.py` script adds sample data automatically:
### Categories
- Sacs à main  
- Bijoux  
- Accessoires pour cheveux  
- Portefeuilles  

### Products
| Name | Stock | Price (€) | Category | Image |
|------|--------|------------|-----------|--------|
| Sac en cuir noir | 10 | 120.0 | Sacs à main | `assets/images/sac_noir.jpg` |
| Bracelet en argent | 15 | 50.0 | Bijoux | `assets/images/bracelet_argent.jpg` |
| Serre-tête fleuri | 25 | 15.0 | Accessoires pour cheveux | `assets/images/serre_tete.jpg` |
| Portefeuille en tissu | 8 | 35.0 | Portefeuilles | `assets/images/portefeuille.jpg` |

---

## ⚙️ How to Run

### Clone the repository
```bash
git clone https://github.com/hancodx/stock-management-App-Python.git
cd stock-management-App-Python
