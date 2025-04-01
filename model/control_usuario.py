from data.conexao import Conexao
from hashlib import sha256


class Usuario:

    def cadastrar(login, senha, nome):

        # criptografia da senha 
        senha = sha256(senha.encode()).hexdigest()

        #cadastrando as informações no banco de dados
        #criando conexão (ponte)
        conexao = Conexao.criar_conexao()

        #usa a conexão que eu criei para buscar as inf do banco de dados(pessoa da ponte)
        cursor  = conexao.cursor()

        #comando sql que será executado
        sql = """INSERT INTO tb_usuarios
                    (login, 
                    senha, 
                    nome)
                VALUES
                    (%s,%s,%s)"""

        #lista com dados
        valores = (login,  senha, nome)

        #executando o comando sql
        cursor.execute(sql,valores)

        #confirma comando
        #se houver alteração/exclusão, confirma a ação de cima
        conexao.commit()

        #é necessário desconectar do banco de dados, fechar a conexão
        cursor.close()
        conexao.close()

    def recuperar_usuario():
        
        #cadastrando as informações no banco de dados
        #criando conexão (ponte)
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary=True)

        #comando sql que será executado
        sql = """select login,
                        senha,
                        nome
                 from tb_usuarios;"""
        
        #executando o comando sql
        cursor.execute(sql)

        # recuperando os dados e colocando em uma variável
        resultado = cursor.fetchall()

        conexao.close()

        return resultado
    
    def logar(login, senha):

        # criptografia da senha
        senha =  sha256(senha.encode()).hexdigest()

        #cadastrando as informações no banco de dados
        #criando conexão (ponte)
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """select * from tb_usuarios 
                 where login = %s
                 and binary senha = %s"""
        
        valores = (login, senha)

        cursor.execute(sql,valores)

        resultado = cursor.fetchone

        if resultado