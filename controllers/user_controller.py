from flask import Blueprint, render_template

user_bp = Blueprint('user_bp', __name__)

# Exemple de route pour la gestion des utilisateurs (cela peut être étendu plus tard)
@user_bp.route('/profile')
def user_profile():
    # Vous pouvez récupérer les informations de l'utilisateur à partir de votre modèle ici
    return render_template('user_profile_view.html')

# Vous pouvez ajouter plus de routes ici pour gérer les actions liées aux utilisateurs
