import sqlite3

con = sqlite3.connect("restaurante.db")

print("PEDIDOS POR DATA")
consulta_datas = """
    SELECT criado_em, COUNT(*) AS quantidade
    FROM pedidos
    GROUP BY criado_em
    ORDER BY criado_em
"""
for linha in con.execute(consulta_datas):
    print(linha)

print()
print("CLIENTES QUE GASTARAM MAIS DE R$ 50,00")
consulta_having = """
    SELECT pedidos.cliente,
           SUM(itens_pedido.quantidade * pratos.preco_centavos) AS total_centavos
    FROM itens_pedido
    JOIN pedidos ON itens_pedido.pedido_id = pedidos.id
    JOIN pratos ON itens_pedido.prato_id = pratos.id
    GROUP BY pedidos.cliente
    HAVING total_centavos > 5000
    ORDER BY total_centavos DESC
"""
for linha in con.execute(consulta_having):
    print(linha)

print()
print("VENDAS DO DIA 2026-11-01 (em centavos)")
consulta_where = """
    SELECT SUM(itens_pedido.quantidade * pratos.preco_centavos) AS total_centavos
    FROM itens_pedido
    JOIN pedidos ON itens_pedido.pedido_id = pedidos.id
    JOIN pratos ON itens_pedido.prato_id = pratos.id
    WHERE pedidos.criado_em = ?
"""
for linha in con.execute(consulta_where, ("2026-11-01",)):
    print(linha)

con.close()