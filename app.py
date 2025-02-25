#importando flask
from flask import Flask
app = Flask (__name__)

# adicionando rotas 
@app.route("/")
def paginaprincipal():
    return "Página Principal"


# ao final de tudo, corrige bugs
app.run(debug=True)