# 📚 API de Livros — Flask + SQLite

Uma API simples de gerenciamento de livros usando **Flask** com persistência em **SQLite** e um front-end integrado via HTML.

---

## ✅ Funcionalidades

- [x] Listar todos os livros
- [x] Buscar livro por ID
- [x] Adicionar novo livro
- [x] Atualizar livro existente
- [x] Deletar livro
- [x] Banco de dados persistente com SQLite
- [x] Front-end incluído e servido via Flask (`/templates/index.html`)

---

## 📦 Requisitos

Instale os pacotes necessários com:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como rodar

```bash
python app.py
```

A aplicação será executada em:

📍 http://127.0.0.1:5000/

---

## 🧠 Tecnologias utilizadas

- Flask
- Flask-CORS
- Flask-SQLAlchemy
- SQLite
- HTML + CSS + JS vanilla

---

## 🧩 Estrutura do Projeto

```
biblioteca_api/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── livros.db (gerado automaticamente)
```

---

## 🔐 CORS

O projeto já vem com CORS habilitado para permitir requisições do front-end.

---

## 🚀 Melhorias futuras sugeridas

- 🔒 Autenticação com JWT
- ✅ Validação de dados com `marshmallow`
- 📁 Separação em módulos (`routes`, `models`, `services`)
- 🧪 Testes com `pytest`
- 📦 Dockerização para facilitar o deploy
