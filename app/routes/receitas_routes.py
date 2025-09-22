from flask import Blueprint, request, jsonify
import app.controllers.receitas_controller as receitas_controller

# Define o Blueprint para as rotas de receitas com um prefixo de URL padrão.
receitas_bp = Blueprint("receitas_bp", __name__, url_prefix="/receitas")

# --- Rotas para a Coleção (/receitas) ---

@receitas_bp.route("/", methods=["GET"])
def listar_receitas():
    """Lista todas as receitas cadastradas."""
    receitas = receitas_controller.listar_receitas()
    return jsonify(receitas), 200

@receitas_bp.route("/cadastrar", methods=["POST"])
def cadastrar_receita():
    """Cria uma nova receita a partir do corpo da requisição JSON.

    Retorna o objeto da nova receita com status 201 em caso de sucesso,
    ou um erro 400 em caso de dados inválidos.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corpo da requisição ausente ou em formato inválido"}), 400
    
    try:
        nova_receita = receitas_controller.cadastrar_receita(data)
        return jsonify(nova_receita), 201 
    except ValueError as e:
        # Captura erros de validação e retorna uma resposta clara
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Captura outros erros inesperados
        return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500

# --- Rotas para um Recurso Específico (/receitas/<id>) ---

@receitas_bp.route("/<string:receita_id>", methods=["GET"])
def buscar_receita(receita_id):
    """Busca e retorna uma receita específica pelo seu ID."""
    receita = receitas_controller.buscar_receita_por_id(receita_id)
    return jsonify(receita), 200

@receitas_bp.route("/<string:receita_id>", methods=["PATCH"])
def atualizar_receita(receita_id):
    """Atualiza parcialmente uma receita a partir do corpo da requisição JSON."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Corpo da requisição ausente ou em formato inválido"}), 400
    try:
        receita_atualizada = receitas_controller.atualizar_receita(receita_id, data)
        return jsonify(receita_atualizada), 200
    except ValueError as e: 
        return jsonify({"error": str(e)}), 400

@receitas_bp.route("/<string:receita_id>", methods=["DELETE"])
def deletar_receita(receita_id):
    """Deleta uma receita específica pelo seu ID. Retorna 204 em caso de sucesso."""
    receitas_controller.deletar_receita(receita_id)
    return "", 204
