#Importando o flask para poder usar no nosso progama
from flask import Flask

#Vamos criar uma variável(neste caso, um objeto) para representar nossa aplicação web
app = Flask(__name__)

#Vamos criar uma rota para acessar o servidor
@app.route("/")
#Ao acessar essa rota a função abaixo é executada e ela devolve (return) o texto "Deu certo!"
def exibir_mensagem():
    return "Deu certo!"

#A linha abaixo executa a aplicação web que foi criada a paritir do flask
app.run(debug=True)