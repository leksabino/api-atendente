import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from modelos import Pedido

CAMINHO_BANCO = "restaurante.db"

app = FastAPI(title="API do Atendente")


class ItemEntrada(BaseModel):
    prato_id: int
    quantidade: int = Field(default=1, ge=1)


class PedidoEntrada(BaseModel):
    cliente: str
    itens: list[ItemEntrada] = Field(min_length=1)


@app.get("/pratos")
def listar_pratos():
    con = sqlite3.connect(CAMINHO_BANCO)
    con.row_factory = sqlite3.Row
    linhas = con.execute(
        "SELECT id, nome, categoria, preco_centavos FROM pratos"
    ).fetchall()
    con.close()
    return [dict(linha) for linha in linhas]


@app.post("/pedidos", status_code=201)
def criar_pedido(dados: PedidoEntrada):
    pedido = Pedido(dados.cliente)
    try:
        for item in dados.itens:
            pedido.adicionar_item(item.prato_id, item.quantidade)
        total = pedido.total_centavos()
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    pedido_id = pedido.salvar()
    return {"id": pedido_id, "cliente": dados.cliente, "total_centavos": total}