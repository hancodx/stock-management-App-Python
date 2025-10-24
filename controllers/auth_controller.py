from flask import render_template, request, redirect, url_for, session, flash
from models.database import Database
import hashlib

class AuthController:
    def __init__(self):
        self.db = Database()

    def hash_password(self, password):
        # Hacher le mot de passe avec SHA256
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            # Récupérer l'utilisateur depuis la base de données
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            hashed_password = self.hash_password(password)
            user = self.db.fetch_one(query, (username, hashed_password))

            if user:
                session['user_id'] = user[0]
                session['username'] = user[1]
                flash('Connexion réussie !', 'success')
                return redirect(url_for('home'))
            else:
                flash('Nom d\'utilisateur ou mot de passe incorrect.', 'danger')

        return render_template('login.html')

    def register(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['confirm_password']

            # Validation des données
            if password != confirm_password:
                flash('Les mots de passe ne correspondent pas.', 'danger')
                return render_template('register.html')

            try:
                # Insérer un nouvel utilisateur dans la base de données
                query = "INSERT INTO users (username, password) VALUES (?, ?)"
                hashed_password = self.hash_password(password)
                self.db.execute_query(query, (username, hashed_password))
                flash('Inscription réussie ! Vous pouvez maintenant vous connecter.', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                flash('Erreur : Ce nom d\'utilisateur est déjà utilisé.', 'danger')

        return render_template('register.html')

    def logout(self):
        session.clear()
        flash('Vous êtes déconnecté.', 'info')
        return redirect(url_for('login'))
