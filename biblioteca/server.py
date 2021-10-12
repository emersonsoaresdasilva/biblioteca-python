from datetime import datetime
from flask import Flask, json, jsonify, request, make_response

biblioteca = Flask(__name__)

obras = [
    {
        "id": 1,
        "titulo": "Como viver com 24 horas por Dia",
        "editora": "Auster",
        "foto": "",
        "autores": ["Bennett, Arnold"]
    },
    {
        "id": 2,
        "titulo": "O Poder do Hábito",
        "editora": "Objetiva",
        "foto": "",
        "autores": ["Charles Duhigg"]
    }
]

@biblioteca.route('/')
def inicio():
    return 'O desafio é criar o backend para um sistema de gerenciamento de uma biblioteca!'

@biblioteca.route('/obras', methods=['POST'])
def cadastra_obra():
    dicionario_retornado = request.json
    if dicionario_retornado in obras:
        return jsonify({'status': 'obra já cadastrada'}), 400
    obras.append(dicionario_retornado)
    return jsonify({'status': 'obra cadastrada'}), 200

@biblioteca.route('/upload-obras', methods=['POST'])
def envia_csv():
    pass

@biblioteca.route('/obras/', methods=['GET'])
def exibe_obras():
    return jsonify(obras)

@biblioteca.route('/file-obras/', methods=['GET'])
def obras_csv():
    dados = 'id;titulo;editora;foto;autores;data_criacao\n'
    for obra in obras:
        dados += f'{obra["id"]};'
        dados += f'{obra["titulo"]};'
        dados += f'{obra["editora"]};'
        dados += f'{obra["foto"]};'
        dados += f'{obra["autores"]};'
        dados += f'{datetime.now().strftime("%d/%m/%Y")}\n'
    csv = make_response(dados)
    csv.headers['Content-Disposition'] = 'attachment; filename=obras.csv'
    csv.mimetype='text/csv'
    return csv

@biblioteca.route('/obras/<int:id>', methods=['PUT'])
def atualiza_obra(id):
    obra_atualizada = request.json
    for obra in obras:
        if obra['id'] == id:
            indice = obras.index(obra)
            obras.remove(obra)
            obras.insert(indice, obra_atualizada)
            return jsonify({'status': 'obra atualizada'}), 200
    return jsonify({'status': 'obra não localizada'}), 404

@biblioteca.route('/obras/<int:id>', methods=['DELETE'])
def remove_obra(id):
    for obra in obras:
        if obra['id'] == id:
            obras.remove(obra)
            return jsonify({'status': 'obra removida'}), 200
    return jsonify({'status': 'obra não localizada'}), 404

if __name__ == '__main__':     
   biblioteca.run(host = 'localhost', port = 5003, debug=True)