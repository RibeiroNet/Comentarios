import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, comentario):  

        data_hora = datetime.datetime.today()

        #cadastrando as informações no banco de dados
        #criando conexão (ponte)
        conexao = mysql.connector.connect(
            host= "127.0.0.1",
            port = 3306,
            user = "root",
            password = "root",
            database = "db_comentarios")

        # 
        conexao = Conexao.criar_conexao()

        #usa a conexão que eu criei para buscar as inf do banco de dados(pessoa da ponte)
        cursor  = conexao.cursor()

        # comando sql que será executado
        sql = """INSERT INTO tb_comentarios
                    (nome, data_hora, comentario)
                VALUES
                    (%s,%s,%s)"""

        # lista com dados
        valores = (usuario,  data_hora, comentario)

        #executando o comando sql
        cursor.execute(sql,valores)

        # confirma comando
        # se houver alteração/exclusão, confirma a ação de cima
        conexao.commit()

        #é necessário desconectar do banco de dados, fechar a conexão
        cursor.close()
        conexao.close()

    def recuperar_mensagens():
        # criar conexão
        conexao = Conexao.criar_conexao()
        # cursor
        cursor = conexao.cursor(dictionary = True)

        sql = """select nome as usuario,
                        data_hora,
                        comentario as mensagem
                        from tb_comentarios"""
 
        # executando o comando 
        cursor.execute(sql)

        #criando variável para guardar os dados em uma variável
        resultado = cursor.fetchall()

        # fechando a conexão
        cursor.close()
        conexao.close()

    