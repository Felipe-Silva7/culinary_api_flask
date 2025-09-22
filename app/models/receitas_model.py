from app.services.firestore import db

class ReceitasModel:
    """
    Gerencia todas as operações de acesso a dados para a coleção 'receitas' no Firestore.
    Esta classe encapsula a lógica de interação com o banco de dados, como criar,
    ler, atualizar e deletar documentos de receitas.
    """
    def __init__(self):
        """Inicializa o model, estabelecendo a conexão com a coleção 'receitas'."""
        self.collection = db.collection("receitas")
    
    def listar_receitas(self):
        """
        Recupera todas as receitas da coleção no Firestore.

        Returns:
            list[dict]: Uma lista de dicionários, onde cada dicionário representa uma receita,
                        incluindo seu ID.
        """
        receitas = self.collection.stream()
        lista_receitas = []
        for receita in receitas:
            dados = receita.to_dict()
            dados['id'] = receita.id
            lista_receitas.append(dados)
        return lista_receitas
    
    def cadastrar_receita(self, data):
        """
        Adiciona um novo documento de receita ao Firestore.

        O Firestore gera um ID único para o novo documento.

        Args:
            data (dict): Um dicionário com os dados da receita a ser criada.
            
        Returns:
            dict: O dicionário da receita recém-criada, já incluindo seu novo ID.
        """
        # O Firestore cria um ID automaticamente se não passarmos um no .document()
        doc_ref = self.collection.document()
        doc_ref.set(data)
        
        # Prepara o objeto de retorno já com o ID
        receita_criada = data
        receita_criada['id'] = doc_ref.id
        
        return receita_criada

    def buscar_por_id(self, receita_id):
        """
        Busca um único documento de receita pelo seu ID.

        Args:
            receita_id (str): O ID do documento a ser procurado.
        
        Returns:
            dict or None: Um dicionário com os dados da receita se encontrada,
                          caso contrário, retorna None.
        """
        doc_ref = self.collection.document(receita_id)
        doc = doc_ref.get()
        
        if doc.exists:
            return {**doc.to_dict(), 'id': doc.id}
        else:
            return None
            
    def atualizar_parcial(self, receita_id, data):
        """
        Atualiza parcialmente um documento de receita existente usando o método update().

        Args:
            receita_id (str): O ID do documento a ser atualizado.
            data (dict): Um dicionário contendo apenas os campos a serem alterados.
            
        Returns:
            dict or None: O dicionário do documento completo e atualizado se a operação
                          for bem-sucedida, ou None se o documento não for encontrado.
        """
        doc_ref = self.collection.document(receita_id)

        # Primeiro, verifica se o documento realmente existe
        if not doc_ref.get().exists:
            return None

        # O método .update() mescla os dados, alterando apenas os campos fornecidos.
        doc_ref.update(data)

        # Retornamos o documento completo após a atualização.
        return {**doc_ref.get().to_dict(), 'id': doc_ref.id}

    def deletar(self, receita_id):
        """
        Deleta um documento de receita do Firestore pelo seu ID.

        Args:
            receita_id (str): O ID do documento a ser deletado.
            
        Returns:
            bool: True se o documento foi encontrado e deletado, False caso contrário.
        """
        doc_ref = self.collection.document(receita_id)

        if not doc_ref.get().exists:
            return False 

        doc_ref.delete()
        return True 