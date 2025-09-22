from flask import Flask
from app.routes.receitas import receita_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(receita_bp)
    return app