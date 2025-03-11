#importando
import datetime
from flask import Flask, render_template, request, redirect
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem

app = Flask (__name__)

# adicionando rotas 
@app.route("/")
def pagina_principal():
    # recuperar mensagem
    Mensagem = Mensagem.recuperar_mensagem()
    return render_template("pagina_principal.html", mensagens = Mensagem)

@app.route("/post/comentario", methods = ["POST"])
def post_comentario():
    #informações vindas do formulário html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")

    # cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)
    # redireciona para o index
    return redirect ("/")

# ao final de tudo, corrige bugs
app.run(debug=True)