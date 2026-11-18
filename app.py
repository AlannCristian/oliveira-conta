from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Oliveira Conta: nosso servidor Python está funcionando!"