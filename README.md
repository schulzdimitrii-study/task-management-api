# Task Management API

API REST simples para gerenciamento de tarefas construída com Flask.

## 🛠️ Tecnologias

- **Python 3.13**
- **Flask 3.1.1** - Framework web
- **Werkzeug 3.1.3** - Servidor WSGI
- **Requests 2.32.5** - Cliente HTTP
- **Pytest 8.4.1** - Framework de testes

## 📁 Estrutura do Projeto

```
task-management-API/
├── app.py              # Aplicação principal Flask
├── models/
│   └── task.py         # Modelo Task
├── requirements.txt    # Dependências
└── README.md
```

## 🏗️ Padrões de Projeto

- **MVC (Model-View-Controller)**: Separação clara entre modelo (`Task`) e controlador (`app.py`)
- **REST API**: Endpoints seguem convenções RESTful
- **Armazenamento em memória**: Lista Python para simplicidade (dados não persistem)

## ⚙️ Setup e Configuração

### 1. Criar ambiente virtual

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

### 2. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 3. Executar aplicação

```powershell
python app.py
```

A API estará disponível em: `http://localhost:5000`

## 📝 Endpoints

| Método | Endpoint      | Descrição               |
| ------ | ------------- | ----------------------- |
| POST   | `/tasks`      | Criar nova tarefa       |
| GET    | `/tasks`      | Listar todas as tarefas |
| GET    | `/tasks/<id>` | Buscar tarefa por ID    |
| PUT    | `/tasks/<id>` | Atualizar tarefa        |
| DELETE | `/tasks/<id>` | Deletar tarefa          |

### Exemplo de uso

```json
POST /tasks
{
    "title": "Estudar Python",
    "description": "Revisar conceitos de Flask",
    "completed": false
}
```

## ⚠️ Observações

- **Dados temporários**: As tarefas são armazenadas em memória e são perdidas ao reiniciar o servidor
- **Ambiente de desenvolvimento**: Configurado com `debug=True`
- **CORS**: Não configurado (adicionar Flask-CORS se necessário para frontend)

## 🧪 Testes

```powershell
pytest
```
