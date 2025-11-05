from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/info')
def info():
    modulo = "CSS"
    aula = "1"
    return f"<h1>Modulo: {modulo}, Aula: {aula}</h1>"

@app.route('/bemvindo/<usuario>')
def bemvindo(usuario):
    return f"<h1>Bem vindo{usuario.capitalize()} </h1>"

@app.get("/sobre") 
def sobre(): 
    return render_template("sobre.html")