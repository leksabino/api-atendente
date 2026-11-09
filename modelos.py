import sqlite3
from datetime import date

CAMINHO_BANCO = "restaurante.db"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = {}

    def adicionar_item(self, prato_id, quantidade=1):
        if quantidade < 1:
            raise ValueError("A quantidade deve ser pelo menos 1.")
        self.itens[prato_id] = self.itens.get(prato_id, 0) + quantidade

    def total_centavos(self):
        con = sqlite3.connect(CAMINHO_BANCO)
        total = 0
        for prato_id, quantidade in self.itens.items():
            linha = con.execute(
                "SELECT preco_centavos FROM pratos WHERE id = ?", (prato_id,)
            ).fetchone()
            if linha is None:
                con.close()
                raise ValueError(f"Não existe prato com id {prato_id}.")
            total += linha[0] * quantidade
        con.close()
        return total

    def salvar(self):
        con = sqlite3.connect(CAMINHO_BANCO)
        cursor = con.execute(
            "INSERT INTO pedidos (cliente, criado_em) VALUES (?, ?)",
            (self.cliente, date.today().isoformat()),
        )
        pedido_id = cursor.lastrowid
        for prato_id, quantidade in self.itens.items():
            con.execute(
                "INSERT INTO itens_pedido (pedido_id, prato_id, quantidade) VALUES (?, ?, ?)",
                (pedido_id, prato_id, quantidade),
            )
        con.commit()
        con.close()
        return pedido_id