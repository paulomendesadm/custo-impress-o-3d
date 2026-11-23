from pathlib import Path
import csv
import sqlite3

pasta = Path(__file__).parent

with sqlite3.connect(":memory:") as banco:
    banco.execute("""
        CREATE TABLE impressoes (
            peca TEXT,
            quantidade_lote INTEGER,
            filamento_g REAL,
            tempo_min INTEGER,
            preco_filamento_kg REAL,
            status TEXT
        )
    """)

    with (pasta / "impressoes.csv").open(encoding="utf-8-sig", newline="") as arquivo:
        linhas = csv.reader(arquivo)
        next(linhas)
        banco.executemany("INSERT INTO impressoes VALUES (?, ?, ?, ?, ?, ?)", linhas)

    consulta = (pasta / "consultas.sql").read_text(encoding="utf-8-sig")
    for peca, custo in banco.execute(consulta):
        valor = f"{custo:.2f}".replace(".", ",")
        print(f"{peca}: R$ {valor}")
        