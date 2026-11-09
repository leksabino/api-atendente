import sqlite3
from cardapio import CARDAPIO

def criar_banco(caminho="restaurante.db"):
    con = sqlite3.connect(caminho)
    con.execute("DROP TABLE IF EXISTS pratos")
    con.execute("""
        CREATE TABLE pratos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            categoria TEXT,
            preco_centavos INTEGER NOT NULL,
            tempo_preparo_min INTEGER,
            ingredientes TEXT,
            alergenicos TEXT,
            vegetariano INTEGER,
            vegano INTEGER
        )
    """)
    for p in CARDAPIO:
        con.execute(
            """INSERT INTO pratos
               (id, nome, categoria, preco_centavos, tempo_preparo_min,
                ingredientes, alergenicos, vegetariano, vegano)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                p["id"],
                p["nome"],
                p["categoria"],
                round(p["preco"] * 100),
                p["tempo_preparo_min"],
                ", ".join(p["ingredientes"]),
                ", ".join(p["alergenicos"]),
                int(p["vegetariano"]),
                int(p["vegano"]),
            ),
        )
    con.commit()
    con.close()

if __name__ == "__main__":
    criar_banco()
    print("Banco criado.")