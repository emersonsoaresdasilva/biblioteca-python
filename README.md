# Desafio Python 📚
O desafio é criar o backend para um sistema de gerenciamento de uma biblioteca!

### Requisitos:
- [x] Deve ser desenvolvido em Python. 🐍

### Rotas da aplicação:

- [x] **POST**/obras:
<p>A rota deverá receber <strong>titulo, editora, foto, e autores</strong> dentro do corpo da requisição.</p>
<p>Ao cadastrar um novo projeto, ele deverá ser armazenado dentro de um objeto no seguinte formato: 

```json
{
  "id": 1,
  "titulo": "Harry Potter",
  "editora": "Rocco",
  "foto": "https://i.imgur.com/UH3IPXw.jpg",
  "autores": ["JK Rowling", "..."]
}
```
- [ ] **POST**/upload-obras: <strong>Não implementei upload-obras pois ainda estou aprendendo sobre o assunto e quis abstrair essa parte.</strong>
  
<p>Está rota deverá receber um arquivo cvs contendo os mesmos parâmetros da rota anterior ms podendo ser salvo em massa no banco de dados.</p>

- [x] **GET**/obras/: A rota deverá listar todas as obras cadastradas:

- [x] **GET**/file-obras/: A rota retornar um arquivo contendo todos as obras, deverá ser possível filtrar pela data de criação.

- [x] **PUT**/obras/:id: : A rota deverá atualizar as informações de titulo, editora, foto e autores da obra com o id presente nos parâmetros da rota.

- [x] **DELETE**/obras/:id: : A rota deverá deletar a obra com o id presente nos parâmetros da rota.

### Ferramentas utilizadas:
- Python. 🐍
- Flask. 🌶️
- Postman. 👨‍🚀

### Executar servidor:
<code>python -m venv venv</code> ⤵

<code>pip install -r requirements.txt</code>

<code>python server.py</code> ✔

### Requisitos para utilizar o script:
- [x] Ter o Python 3 instalado na máquina. ✔