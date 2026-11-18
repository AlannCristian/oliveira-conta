from flask import Flask, render_template, request, redirect, url_for
from banco import salvar_contato

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contato", methods=["POST"])
def contato():
    nome = request.form.get("nome", "").strip()
    email = request.form.get("email", "").strip()
    servico = request.form.get("servico", "").strip()

    servicos_permitidos = {"abertura", "mei", "contabilidade"}

    if not nome or not email or not servico:
        return render_template(
            "index.html",
            mensagem="Preencha todos os campos.",
        ), 400

    if len(nome) > 100 or len(email) > 150:
        return render_template(
            "index.html",
            mensagem="Nome ou e-mail ultrapassou o tamanho permitido.",
        ), 400

    if servico not in servicos_permitidos:
        return render_template(
            "index.html",
            mensagem="Selecione um serviço válido.",
        ), 400
        
    salvar_contato(nome, email, servico)

    return redirect(url_for("contato_confirmado"), code=303)

@app.route("/contato/confirmado")
def contato_confirmado():
    return render_template(
        "index.html",
        mensagem="Contato de teste salvo com sucesso!",
    )