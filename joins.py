import sqlite3

con = sqlite3.connect("restaurante.db")

consulta = """
    SELECT pedidos.cliente, pratos.nome, itens_pedido.quantidade
    FROM itens_pedido
    JOIN pedidos ON itens_pedido.pedido_id = pedidos.id
    JOIN pratos ON itens_pedido.prato_id = pratos.id
"""

for linha in con.execute(consulta):
    print(linha)

con.close()