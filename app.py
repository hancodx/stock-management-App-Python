from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from controllers.product_controller import ProductController
from controllers.category_controller import CategoryController
from models.product_model import ProductModel  



app = Flask(__name__)

# Configurer l'upload des fichiers
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Dossier où vous voulez stocker les images
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Extensions autorisées

# Créer le dossier de téléchargement si il n'existe pas
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

product_controller = ProductController()
category_controller = CategoryController()


# Fonction pour vérifier les extensions de fichier
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    # Récupérer les produits depuis la base de données via le contrôleur
    products = product_controller.get_products()

    # Vérifiez si la liste des produits est vide ou non
    if products:
        print(f"Produits trouvés : {products}")
    else:
        print("Aucun produit trouvé dans la base de données")

    # Passer les produits au template
    return render_template('index.html', products=products)


@app.route('/categories')
def list_categories():
    categories = category_controller.get_categories()
    return render_template('categories/list.html', categories=categories)


@app.route('/add-category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        category_controller.add_category(name)
        return redirect(url_for('list_categories'))
    return render_template('categories/add.html')

@app.route('/edit-category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    if request.method == 'POST':
        name = request.form['name']
        category_controller.update_category(category_id, name)
        return redirect(url_for('list_categories'))

    category = category_controller.get_category_by_id(category_id)
    return render_template('categories/edit.html', category=category)

@app.route('/delete-category/<int:category_id>', methods=['GET'])
def delete_category(category_id):
    category_controller.delete_category(category_id)
    return redirect(url_for('list_categories'))


@app.route('/products')
def products_list():
    products = product_controller.get_products()
    return render_template('products/list.html', products=products)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']

        # Vérification et sauvegarde de l'image
        if 'image_path' in request.files:
            image_file = request.files['image_path']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
            else:
                image_path = None
        else:
            image_path = None

        # Ajouter un produit dans la base de données avec le chemin de l'image
        product_controller.add_product(name, price, stock, image_path)
        return redirect(url_for('products_list'))
    return render_template('products/add-product.html')

@app.route('/edit-product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = ProductModel.get_product_by_id(id)  # Appeler la méthode de ProductModel

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']

        # Gestion de l'image si un nouveau fichier est sélectionné
        if 'image_path' in request.files:
            image_file = request.files['image_path']
            if image_file and allowed_file(image_file.filename):
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                image_file.save(image_path)
            else:
                image_path = product[4]  # Garder l'ancienne image si aucune nouvelle image
        else:
            image_path = product[4]  # Garder l'ancienne image si aucune nouvelle image

        # Modifier le produit dans la base de données via ProductModel
        ProductModel.update_product(id, name, price, stock, image_path)

        return redirect(url_for('products_list'))

    return render_template('products/edit-product.html', product=product)

    
@app.route('/delete-product/<int:id>', methods=['GET'])
def delete_product(id):
    # Supprimer le produit
    product_controller.delete_product(id)
    return redirect(url_for('products_list'))


if __name__ == "__main__":
    app.run(debug=True)
