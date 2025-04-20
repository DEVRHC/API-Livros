from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

def inicializar_banco():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{"id": l.id, "titulo": l.titulo, "autor": l.autor} for l in livros])

@app.route('/livros/<int:id>', methods=['GET'])
def buscar_livro(id):
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify({"id": livro.id, "titulo": livro.titulo, "autor": livro.autor})

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    data = request.get_json()
    novo = Livro(id=data['id'], titulo=data['titulo'], autor=data['autor'])
    db.session.add(novo)
    db.session.commit()
    return jsonify({"id": novo.id, "titulo": novo.titulo, "autor": novo.autor}), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    data = request.get_json()
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404
    livro.titulo = data['titulo']
    livro.autor = data['autor']
    db.session.commit()
    return jsonify({"id": livro.id, "titulo": livro.titulo, "autor": livro.autor})

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = db.session.get(Livro, id)
    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404
    db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro deletado com sucesso!"})

if __name__ == '__main__':
    inicializar_banco()
    app.run(debug=True)