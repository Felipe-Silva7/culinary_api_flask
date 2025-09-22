from app.models.receitas_model import ReceitasModel
from flask import abort

# A instância do model é criada uma vez e reutilizada pelos controllers.
# Isso é eficiente e segue o padrão de centralizar o acesso aos dados.
receitas_model = ReceitasModel()

def listar_receitas():
    """
    Orquestra a busca e o retorno de todas as receitas.

    Returns:
        list[dict]: Uma lista de dicionários, onde cada um representa uma receita.
    """
    return receitas_model.listar_receitas()

def cadastrar_receita(data):
    """
    Valida os dados de entrada e orquestra a criação de uma nova receita.

    Args:
        data (dict): O dicionário contendo os dados da nova receita,
                     vindo do corpo da requisição JSON.

    Returns:
        dict: O dicionário da receita recém-criada, incluindo seu ID.

    Raises:
        ValueError: Se algum dos campos obrigatórios estiver ausente ou vazio.
    """

    required_fields = ["titulo", "ingredientes", "modo_preparo"] # Exemplo com mais campos
    missing_fields = [field for field in required_fields if field not in data or not data[field]]

    if missing_fields:
        raise ValueError(f"Campos obrigatórios ausentes ou vazios: {', '.join(missing_fields)}")

    return receitas_model.cadastrar_receita(data)

def buscar_receita_por_id(receita_id):
    """
    Busca uma receita específica pelo seu ID.

    Aborta a requisição com um status HTTP 404 se a receita não for encontrada,
    garantindo que a rota retorne a resposta correta.

    Args:
        receita_id (str): O ID da receita a ser buscada.

    Returns:
        dict: O dicionário contendo os dados da receita encontrada.
    """
    receita = receitas_model.buscar_por_id(receita_id)

    if receita is None:
        abort(404, description=f"Receita com ID '{receita_id}' não encontrada.")
    return receita

def atualizar_receita(receita_id, data):
    """
    Valida os dados e orquestra a atualização parcial de uma receita.

    Args:
        receita_id (str): O ID da receita a ser atualizada.
        data (dict): Um dicionário contendo apenas os campos a serem alterados.

    Returns:
        dict: O objeto completo da receita após a atualização.

    Raises:
        ValueError: Se o corpo da requisição estiver vazio ou não contiver campos válidos.
    
    Aborts:
        404: Se a receita com o ID fornecido não for encontrada.
    """
    if not data:
        raise ValueError("O corpo da requisição não pode ser vazio para uma atualização.")

    allowed_fields = {"titulo", "ingredientes", "modo_preparo", "tempo_preparo"}
    
    # Cria um dicionário apenas com os campos válidos que foram enviados pelo usuário
    update_data = {key: value for key, value in data.items() if key in allowed_fields}

    if not update_data:
        raise ValueError(f"Nenhum campo válido para atualização foi fornecido. Campos permitidos: {', '.join(allowed_fields)}")

    receita_atualizada = receitas_model.atualizar_parcial(receita_id, update_data)
    
    if receita_atualizada is None:
        abort(404, description=f"Receita com ID '{receita_id}' não encontrada para atualização.")
    
    return receita_atualizada

def deletar_receita(receita_id):
    """
    Orquestra a deleção de uma receita pelo seu ID.

    Não retorna nada em caso de sucesso, mas aborta a requisição com 404
    se a receita não for encontrada.

    Args:
        receita_id (str): O ID da receita a ser deletada.
    
    Aborts:
        404: Se a receita com o ID fornecido não for encontrada.
    """
    sucesso = receitas_model.deletar(receita_id)
    if not sucesso:
        abort(404, description=f"Receita com ID '{receita_id}' não encontrada para deleção.")
