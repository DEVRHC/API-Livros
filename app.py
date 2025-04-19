from flask import Flask, jsonify, request

app = Flask(__name__)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base de dados simulada (em memória)
livros = [
    {"id": 1, "titulo": "1984", "autor": "George Orwell"},
    {"id": 2, "titulo": "Dom Casmurro", "autor": "Machado de Assis"}
]

# Rota principal
@app.route('/')
def home():
    return "API de Livros - Bem-vindo!"

# Listar todos os livros
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)

# Buscar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

# Adicionar um novo livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# Atualizar um livro
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            dados = request.get_json()
            livro.update(dados)
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

# Deletar um livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    for i, livro in enumerate(livros):
        if livro["id"] == id:
            del livros[i]
            return jsonify({"mensagem": "Livro deletado com sucesso!"})
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
