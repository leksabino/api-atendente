import sqlite3
import pytest
import modelos
from banco import criar_banco
from modelos import Pedido


@pytest.fixture
def banco_temporario(tmp_path, monkeypatch):
    caminho = str(tmp_path / "teste.db")
    criar_banco(caminho)
    con = sqlite3.connect(caminho)
    con.execute(
        "CREATE TABLE pedidos (id INTEGER PRIMARY KEY, cliente TEXT NOT NULL, criado_em TEXT NOT NULL)"
    )
    con.execute(
        "CREATE TABLE itens_pedido (id INTEGER PRIMARY KEY, pedido_id INTEGER NOT NULL, prato_id INTEGER NOT NULL, quantidade INTEGER NOT NULL)"
    )
    con.commit()
    con.close()
    monkeypatch.setattr(modelos, "CAMINHO_BANCO", caminho)
    return caminho


def test_total_soma_itens(banco_temporario):
    pedido = Pedido("Teste")
    pedido.adicionar_item(1, 2)
    pedido.adicionar_item(4)
    assert pedido.total_centavos() == 8800


def test_quantidade_invalida(banco_temporario):
    pedido = Pedido("Teste")
    with pytest.raises(ValueError):
        pedido.adicionar_item(1, 0)


def test_prato_inexistente(banco_temporario):
    pedido = Pedido("Teste")
    pedido.adicionar_item(99)
    with pytest.raises(ValueError):
        pedido.total_centavos()


def test_salvar_grava_no_banco(banco_temporario):
    pedido = Pedido("Teste")
    pedido.adicionar_item(1, 2)
    pedido_id = pedido.salvar()
    con = sqlite3.connect(banco_temporario)
    linha = con.execute(
        "SELECT cliente FROM pedidos WHERE id = ?", (pedido_id,)
    ).fetchone()
    con.close()
    assert linha[0] == "Teste"