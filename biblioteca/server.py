import sql as db
from datetime import datetime
from flask import Flask, json, jsonify, request, make_response

biblioteca = Flask(__name__)

@biblioteca.route('/')
def inicio():
    return 'O desafio é criar o backend para um sistema de gerenciamento de uma biblioteca!'

@biblioteca.route('/obras', methods=['POST'])
def cadastra_obra():
    db.cria_obra(request.json)
    return jsonify({'status': 'obra cadastrada'}), 200

@biblioteca.route('/upload-obras', methods=['POST'])
def envia_csv():
    pass

@biblioteca.route('/obras/', methods=['GET'])
def exibe_obras():
    return jsonify(db.mostra_obras()) if db.mostra_obras() else jsonify({'status': 'não há obras cadastradas'}), 404

@biblioteca.route('/file-obras/', methods=['GET'])
def obras_csv():
    dados = 'id;titulo;editora;foto;autores;data_criacao\n'
    for obra in db.mostra_obras():
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
    db.atualizada_obra(request.json, id)
    return jsonify({'status': 'obra atualizada'}), 200

@biblioteca.route('/obras/<int:id>', methods=['DELETE'])
def remove_obra(id): 
    db.remove_obra(id)
    return jsonify({'status': 'obra removida'}), 200

if __name__ == '__main__':
    db.reseta_obras()
    biblioteca.run(host = 'localhost', port = 5003, debug=True)