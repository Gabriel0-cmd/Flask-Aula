from flask import Flask

app = Flask(__name__)

@app.route('/info')
def info():
    modulo = "CSS"
    aula = "1"
    return "<h1>pagina info</h1>"

@app.route('/')
def index():
    return f"<h1>Modulo: {modulo}, Aula: {aula}</h1>"

@app.route('/bemvindo/usuario')
def bemvindo(usuario):
    return f"<h1>Bem vindo{usuario.capitalize()} </h1>"