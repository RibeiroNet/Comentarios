#importando flask, data e hora 
import datetime
from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask (__name__)

# adicionando rotas 
@app.route("/")
def pagina_principal():
    return render_template("pagina_principal.html")

@app.route("/post/comentario", methods = ["POST"])
def post_comentario():
    #informações vindas do formulário html
    usuario = request.form.get("usuario")
    comentario = request.form.get("comentario")
    data_hora = datetime.datetime.today()

    #cadastranbdo as informações no banco de dados
    #criando conexão (ponte)
    conexao = mysql.connector.connect(
        host= "127.0.0.1",
        port = 3306,
        user = "root",
        password = "root",
        database = "db_comentarios")

    #usa a conexão que eu criei para buscar as inf do banco de daods(pessoa da ponte)
    cursor  = conexao.cursor()

    # comando sql qe será executado
    sql = """INSERT INTO tb_comentarios
                (nome, data_hora, comentario)
            VALUES
                (%s,%s,%s)"""

    # lista com dados
    valores = (usuario,  data_hora, comentario)

    #executando o comando sql
    cursor.execute(sql,valores)

    conexao.commit()

    #é necessário desconectar do banco de dados, fechar a noexão
    cursor.close()
    conexao.close()


    # redireciona para o index
    return redirect ("/")



# ao final de tudo, corrige bugs
app.run(debug=True)