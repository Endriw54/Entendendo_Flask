#Vamos criar um dicionario com duas chaves e tentar retornar seus dados pela rota
dicionario = {
    "nome":"Endriw Oliveira",
    "nascimento":2005
}


#Importar flask
from flask import Flask
#criar a aplicação Flask
app = Flask(__name__)

#A rota abaixo aciona uma função que retorna um dicionario
@app.route("/teste")
def mostra_dicionario():
    return dicionario

@app.route("/")
def dados_usuario():
    return f"<b>O usuário{dicionario['nome']} nasceu em {dicionario['nascimento']}</b>"

#Colocar a aplicação para rodar
app.run(debug=True)