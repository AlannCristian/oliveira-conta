from flask import Flask, render_template, request, redirect, url_for
from banco import salvar_contato
from email_validator import validate_email, EmailNotValidError
from sqlite3 import Error as SQLiteError

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contato", methods=["POST"])
def contato():
    dados = {
        "nome": request.form.get("nome", "").strip(),
        "email": request.form.get("email", "").strip(),
        "servico": request.form.get("servico", "").strip(),
    }

    servicos_permitidos = {"abertura", "mei", "contabilidade"}
    erro = None

    if not all(dados.values()):
        erro = "Preencha todos os campos."

    elif len(dados["nome"]) > 100 or len(dados["email"]) > 150:
        erro = "Nome ou e-mail ultrapassou o tamanho permitido."

    elif dados["servico"] not in servicos_permitidos:
        erro = "Selecione um serviço válido."

    else:
        try:
            email_validado = validate_email(
                dados["email"],
                check_deliverability=False,
            )

            dados["email"] = email_validado.normalized

        except EmailNotValidError:
            erro = "Informe um e-mail com formato válido."

    if erro:
        return render_template(
            "index.html",
            mensagem=erro,
            tipo_mensagem="erro",
            dados=dados,
        ), 400

    try:
            
        salvar_contato(
            dados["nome"],
            dados["email"],
            dados["servico"],
        )

    except SQLiteError:
        app.logger.exception("Falha ao salvar contato no SQLite.")

        return render_template(
            "index.html",
            mensagem=(
                "Não foi possível salvar seu contato agora. "
                "Tente novamente em alguns instantes."
            ),
            tipo_mensagem="erro",
            dados=dados,
        ), 500

    return redirect(url_for("contato_confirmado"), code=303)

    
@app.route("/contato/confirmado")
def contato_confirmado():
    return render_template(
        "index.html",
        mensagem="Contato de teste salvo com sucesso!",
        tipo_mensagem="sucesso",
    )