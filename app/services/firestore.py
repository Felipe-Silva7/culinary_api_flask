import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

try:
    # Obtém o caminho para o arquivo de credenciais da Service Account 
    cred = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    # Inicializa o Firebase Admin SDK apenas se ainda não estiver inicializado
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred)
        firebase_admin.initialize_app(cred)

    # Cria uma instância do cliente Firestore
    db = firestore.client()
    print("Cliente Firestore conectado.")

except FileNotFoundError as e:
    print(f"ERRO: {e}")
    print("Verifique se o caminho para o arquivo JSON das credenciais está correto.")
    exit()
except Exception as e:
    print(f"Erro ao inicializar o Firebase Admin SDK: {e}")
    exit()