#importando
import datetime
from flask import Flask, render_template, request, redirect
import mysql.connector
from data.conexao import Conexao
from model.control_mensagem import Mensagem
from model.control_usuario import Usuario

app = Flask (__name__)

#rotas 
@app.route("/comentario")
def pagina_principal():
    # recuperar mensagem
    Mensagens = Mensagem.recuperar_mensagens()
    return render_template("pagina_principal.html", mensagens = Mensagens)

@app.route("/post/comentario", methods = ["POST"])
def post_comentario(usuario, comentario):
    #informações vindas do formulário html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")

    # cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastrar_mensagem()
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

@app.route("/")
def cadastro_usuario():
    # recupera o usuário
    usuarios = Usuario.recuperar_usuario()

    return render_template("pagina_login.html", usuarios = usuarios)

@app.route("/post/cadastrarusuario", methods = ["GET"])
def post_usuario():
    # pego as informações vindas do usuário
    login = request.form.get("login")
    senha = request.form.get("senha")  
    nome = request.form.get("nome")
   
    # cadastrando a mensagem usando a class mensagem 
    Usuario.cadastrar(login, senha, nome)

    return redirect("/pagina_login")



# ao final de tudo, corrige bugs
app.run(debug=True)