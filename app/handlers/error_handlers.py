from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    """
    Registra os manipuladores de erro globais para a aplicação Flask.

    Esta função centraliza o tratamento de erros HTTP comuns, garantindo que
    a API sempre retorne respostas em formato JSON, mesmo em caso de erro.

    Args:
        app (Flask): A instância da aplicação Flask onde os handlers serão registrados.
    """
    @app.errorhandler(404)
    def handle_not_found_error(error):
        """Captura erros 404 (Not Found) e retorna uma resposta JSON."""
        response = {
            "error": "Recurso não encontrado",
            "message": error.description  # Mensagem customizada do abort()
        }
        return jsonify(response), 404

    @app.errorhandler(400)
    def handle_bad_request_error(error):
        """Captura erros 400 (Bad Request) e retorna uma resposta JSON."""
        response = {
            "error": "Requisição inválida",
            "message": error.description
        }
        return jsonify(response), 400
    
    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        """
        Captura todas as outras exceções para evitar que erros internos exponham
        detalhes da aplicação, retornando sempre um erro 500 em JSON.
        """
        # Se for um erro HTTP padrão (gerado pelo abort()), use seus detalhes
        if isinstance(error, HTTPException):
            response = {
                "error": error.name,
                "message": error.description
            }
            return jsonify(response), error.code
        
        # Para erros inesperados do código, uma mensagem genérica é mais segura
        response = {
            "error": "Internal Server Error",
            "message": "Ocorreu um erro inesperado no servidor."
        }
        # É uma boa prática logar o erro real para fins de depuração
        app.logger.error(f"Erro não tratado: {error}")
        return jsonify(response), 500