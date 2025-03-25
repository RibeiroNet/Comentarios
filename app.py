#importando
import datetime
from flask import Flask, render_template, request, redirect
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
app = Flask (__name__)

#rotas 
@app.route("/")
def pagina_principal():
    # recuperar mensagem
    Mensagens = Mensagem.recuperar_mensagens()
    return render_template("pagina_principal.html", mensagens = Mensagens)

@app.route("/post/comentario", methods = ["POST"])
def post_comentario():
    #informações vindas do formulário html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")

    # cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem(usuario, comentario)
    # redireciona para o index
    return redirect ("/")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/")

@app.route("/put/mensagem/curtir/<codigo>")
def add_curtida(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/")

@app.route("/put/mensagem/descurtir/<codigo>")
def deslike(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect("/")    

# ao final de tudo, corrige bugs
app.run(debug=True)