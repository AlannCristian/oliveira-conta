from flask import Flask, render_template, request

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

    return render_template(
        "index.html",
        mensagem="Dados recebidos pelo Python! Ainda não foram salvos.",
    )