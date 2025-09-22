from flask import Blueprint

# Define o blueprint da rota principal de receitas
receita_bp = Blueprint("receita_bp", __name__)

# Rota raiz da API — usada para teste de disponibilidade
@receita_bp.route("/")
def index():
    return "ok"