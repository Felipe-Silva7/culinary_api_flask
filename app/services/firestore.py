import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import json

try:
    # Obtém o caminho para o arquivo de credenciais da Service Account 
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

    # Inicializa o Firebase Admin SDK apenas se ainda não estiver inicializado
    if not firebase_admin._apps:
        cred = credentials.Certificate(json.loads(cred))
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