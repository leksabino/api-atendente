import sqlite3

con = sqlite3.connect("restaurante.db")

con.execute("DROP TABLE IF EXISTS itens_pedido")
con.execute("DROP TABLE IF EXISTS pedidos")

con.execute("""
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY,
        cliente TEXT NOT NULL,
        criado_em TEXT NOT NULL
    )
""")
con.execute("""
    CREATE TABLE itens_pedido (
        id INTEGER PRIMARY KEY,
        pedido_id INTEGER NOT NULL,
        prato_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
        FOREIGN KEY (prato_id) REFERENCES pratos(id)
    )
""")

pedidos = [
    (1, "Ana", "2026-11-01"),
    (2, "Bruno", "2026-11-01"),
    (3, "Carla", "2026-11-02"),
]
itens = [
    (1, 1, 2),
    (1, 4, 1),
    (2, 2, 1),
    (2, 3, 1),
    (2, 4, 2),
    (3, 1, 1),
]

con.executemany(
    "INSERT INTO pedidos (id, cliente, criado_em) VALUES (?, ?, ?)", pedidos
)
con.executemany(
    "INSERT INTO itens_pedido (pedido_id, prato_id, quantidade) VALUES (?, ?, ?)",
    itens,
)
con.commit()

print("PEDIDOS")
for linha in con.execute("SELECT * FROM pedidos"):
    print(linha)

print("ITENS")
for linha in con.execute("SELECT * FROM itens_pedido"):
    print(linha)

con.close()