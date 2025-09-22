from flask import Blueprint
from app.services.firestore import db

# Define o blueprint da rota principal de receitas
receita_bp = Blueprint("receita_bp", __name__)

# Rota raiz da API — usada para teste de disponibilidade
@receita_bp.route("/")
def index():
    return "ok"

# Rota apenas para testar a conexão com o Firestore
@receita_bp.route("/receitas")
def receitas():
    receitas = db.collection("receitas").stream()
    for receita in receitas:     
        return f"{receita.id} => {receita.to_dict()}"