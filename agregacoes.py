import sqlite3

con = sqlite3.connect("restaurante.db")

print("TOTAL POR CLIENTE (em centavos)")
consulta_clientes = """
    SELECT pedidos.cliente,
           SUM(itens_pedido.quantidade * pratos.preco_centavos) AS total_centavos
    FROM itens_pedido
    JOIN pedidos ON itens_pedido.pedido_id = pedidos.id
    JOIN pratos ON itens_pedido.prato_id = pratos.id
    GROUP BY pedidos.cliente
    ORDER BY total_centavos DESC
"""
for linha in con.execute(consulta_clientes):
    print(linha)

print()
print("PRATOS MAIS VENDIDOS")
consulta_pratos = """
    SELECT pratos.nome,
           SUM(itens_pedido.quantidade) AS unidades
    FROM itens_pedido
    JOIN pratos ON itens_pedido.prato_id = pratos.id
    GROUP BY pratos.nome
    ORDER BY unidades DESC, pratos.nome
"""
for linha in con.execute(consulta_pratos):
    print(linha)

con.close()