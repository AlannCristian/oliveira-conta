import sqlite3
from contextlib import closing
from pathlib import Path

CAMINHO_BANCO = Path(__file__).resolve().parent / "contatos.db"


def criar_tabelas():
    with closing(sqlite3.connect(CAMINHO_BANCO)) as conexao:
        with conexao:
            conexao.execute("""
                CREATE TABLE IF NOT EXISTS contatos (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    servico TEXT NOT NULL,
                    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)


if __name__ == "__main__":
    criar_tabelas()
    print("Banco e tabela de contatos preparados.")