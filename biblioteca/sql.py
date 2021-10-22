from sqlalchemy import create_engine

engine = create_engine('sqlite:///biblioteca.db')

with engine.connect() as conexao:
    create_obras = '''
    CREATE TABLE IF NOT EXISTS Obra(
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        editora TEXT,
        foto TEXT,
        autores TEXT
    )
    '''
    resposta = conexao.execute(create_obras)

def cria_obra(dicionario):
    with engine.connect() as conexao:
        sql = f'INSERT INTO Obra (titulo, editora, foto, autores) VALUES (:titulo, :editora, :foto, :autores)'
        conexao.execute(
            sql,
            titulo=dicionario['titulo'],
            editora=dicionario['editora'],
            foto=dicionario['foto'],
            autores=dicionario['autores']
        )

def mostra_obras():
    with engine.connect() as conexao:
        sql = 'SELECT * FROM Obra'
        resposta = conexao.execute(sql)
        obras = []
        while True:
            linha = resposta.fetchone()
            if linha is None:
                break
            obras.append(dict(linha))
        return obras

def remove_obra(id):
    with engine.connect() as conexao:
        sql = 'DELETE FROM Obra WHERE id = :id'
        conexao.execute(sql, id=id)

def atualizada_obra(dicionario, id):
    with engine.connect() as conexao:
        sql = 'UPDATE Obra SET titulo = :titulo, editora = :editora, foto = :foto, autores = :autores WHERE id = :id'
        conexao.execute(
            sql,
            titulo=dicionario['titulo'],
            editora=dicionario['editora'],
            foto=dicionario['foto'],
            autores=dicionario['autores'],
            id=id
        )

def reseta_obras():
    with engine.connect() as conexao:   
        sql = 'DELETE FROM Obra' 
        conexao.execute(sql)
