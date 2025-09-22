from flask import Flask
from app.routes.receitas_routes import  receitas_bp
from app.handlers import error_handlers # Importa o módulo

def create_app():
    """
    Cria e configura uma instância da aplicação Flask.

    Esta função segue o padrão Application Factory. Ela é responsável por:
    1. Inicializar a aplicação Flask.
    2. Registrar os blueprints que contêm as rotas da API.
    3. Registrar os manipuladores de erro globais para garantir respostas JSON consistentes.

    Returns:
        Flask: A instância configurada da aplicação, pronta para ser executada.
    """
    app = Flask(__name__)

    # NOTA: Em uma aplicação de produção, a configuração (chaves secretas, etc.)
    # seria carregada a partir de um arquivo ou variáveis de ambiente aqui.
    # Ex: app.config.from_object('config.ProductionConfig')

    # Anexa o conjunto de rotas de receitas à aplicação principal.
    app.register_blueprint(receitas_bp)

    # Anexa os handlers que padronizam as respostas de erro da API.
    error_handlers.register_error_handlers(app)

    return app