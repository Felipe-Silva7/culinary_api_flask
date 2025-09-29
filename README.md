# 🍳 Culinary API - Flask & Firestore

API RESTful para gerenciamento de **receitas culinárias**, desenvolvida com **Python**, **Flask** e **Google Firestore**.  
O projeto foi estruturado seguindo **boas práticas de arquitetura de software**, aplicando o padrão **MVC+S (Model-View-Controller + Service)** e o design pattern **Application Factory**, garantindo escalabilidade e organização do código.

A API está hospedada e disponível na plataforma **Render**.

📄 [Apresentação da API (PDF)](Construindo APIs escaláveis com Flask, Firestore e Render.pdf)


---

## 🚀 Live Demo

- **URL Base:** [https://culinary-api-flask.onrender.com](https://culinary-api-flask.onrender.com)

---

## ✨ Principais Features

- **CRUD Completo** → Criar, Ler, Atualizar (parcial) e Deletar receitas.  
- **Arquitetura RESTful** → Endpoints padronizados conforme convenções REST.  
- **Código Organizado** → Separação clara de responsabilidades (MVC + Service).  
- **Application Factory** → Modularidade para testes e múltiplos ambientes.  
- **Tratamento de Erros Centralizado** → Respostas JSON consistentes.  
- **Pronto para Produção** → Deploy com **Gunicorn** para maior performance.  
- **Banco de Dados Escalável** → Uso do **Google Firestore (NoSQL serverless)**.  

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.10, Flask  
- **Banco de Dados:** Google Firestore  
- **Servidor de Produção:** Gunicorn  
- **Deploy:** Render  
- **Gerenciamento de Dependências:** `pip` + `requirements.txt`  
- **Variáveis de Ambiente:** `python-dotenv`  

---

## 🔧 Como Executar Localmente

### Pré-requisitos

- Python **3.10+**  
- Conta no **Google Cloud** com **Firestore ativado**  
- Arquivo de **credenciais da Conta de Serviço** (JSON) do Firebase  

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie e ative um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scriptsctivate      # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**

   Crie um arquivo **.env** na raiz do projeto com o seguinte conteúdo:

   ```
   GOOGLE_APPLICATION_CREDENTIALS="caminho/para/seu/arquivo-de-credenciais.json"
   ```

5. **Execute a aplicação**
   ```bash
   python run.py
   ```

➡️ A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Como Testar a API (Postman)

1. Crie uma **Collection** no Postman.  
2. Defina a variável `baseUrl` na aba **Variables** como:
   ```
   https://culinary-api-flask.onrender.com
   ```
3. Use os endpoints substituindo a URL por `{{baseUrl}}`.

### Exemplos de Requisição

#### 1. Criar Receita (POST)
- **URL:** `{{baseUrl}}/receitas`  
- **Headers:** `Content-Type: application/json`  
- **Body:**
  ```json
  {
    "titulo": "Bolo de Cenoura da Vovó",
    "ingredientes": [
      "3 cenouras médias",
      "4 ovos",
      "1/2 xícara de óleo",
      "2 xícaras de açúcar",
      "2 1/2 xícaras de farinha de trigo",
      "1 colher de sopa de fermento em pó"
    ],
    "modo_preparo": "Bata os líquidos e o açúcar no liquidificador. Misture com a farinha e o fermento. Asse por 40 minutos.",
    "tempo_preparo": "60 minutos"
  }
  ```

---

#### 2. Listar Receitas (GET)
- **URL:** `{{baseUrl}}/receitas`

---

#### 3. Buscar Receita por ID (GET)
- **URL:** `{{baseUrl}}/receitas/:id`

---

#### 4. Atualizar Receita (PATCH)
- **URL:** `{{baseUrl}}/receitas/:id`  
- **Body:**
  ```json
  {
    "titulo": "O Melhor Bolo de Cenoura do Mundo",
    "tempo_preparo": "55 minutos"
  }
  ```

---

#### 5. Deletar Receita (DELETE)
- **URL:** `{{baseUrl}}/receitas/:id`

---

## 📂 Estrutura do Projeto

```
├── app/
│   ├── __init__.py         # Application Factory (create_app)
│   ├── controllers/        # Lógica das requisições (Camada C)
│   ├── handlers/           # Tratamento global de erros
│   ├── models/             # Interação com o Firestore (Camada M)
│   └── routes/             # Definição de rotas e endpoints (Camada V)
├── requirements.txt        # Dependências do projeto
└── run.py                  # Ponto de entrada da aplicação
```

👨‍💻 Desenvolvido por - **Antônio Felipe** – [@Felipe-Silva7](https://github.com/Felipe-Silva7)
