# API do Atendente

API REST em Python (FastAPI) para um atendente de restaurante. Lista o cardápio e registra pedidos em um banco SQLite, com a lógica do pedido em uma classe `Pedido` e testes automatizados com pytest.

É a continuação do [atendente-restaurante-ia](https://github.com/leksabino/atendente-restaurante-ia), onde montei um agente de IA com function calling. Aqui o foco é a camada de dados e de API: SQL com `JOIN` e `GROUP BY`, orientação a objetos e testes.

## O que ela faz

- `GET /pratos`: lista os pratos do cardápio
- `POST /pedidos`: cria um pedido com um ou mais itens, calcula o total e grava no banco
- Valida a entrada: quantidade menor que 1 ou pedido sem itens é recusado com **422**
- Recusa prato inexistente com **400** e uma mensagem clara, sem gravar nada
- Documentação interativa gerada automaticamente em `/docs`

## Como funciona

```
cardapio.py ──> banco.py ──> restaurante.db
                                  │
                  modelos.py (classe Pedido)
                                  │
                       api.py (FastAPI)  <──  requisições HTTP
```

A classe `Pedido` guarda os itens, calcula o total em centavos inteiros consultando os preços no banco, e salva o pedido e seus itens. A API só valida a entrada e chama a classe.

## Exemplo de uso

`POST /pedidos` com:

```json
{
  "cliente": "Maria",
  "itens": [
    {"prato_id": 1, "quantidade": 2},
    {"prato_id": 4}
  ]
}
```

Resposta (**201**):

```json
{"id": 5, "cliente": "Maria", "total_centavos": 8800}
```

## Como rodar

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie o banco e as tabelas de pedidos (com alguns pedidos de exemplo):

```bash
python banco.py
python sql_pratica.py
```

4. Suba a API e abra `http://127.0.0.1:8000/docs`:

```bash
uvicorn api:app --reload
```

5. Rode os testes:

```bash
pytest -v
```

## Estudos de SQL

Os scripts abaixo rodam consultas sobre as tabelas `pedidos`, `itens_pedido` e `pratos`:

- `joins.py`: `JOIN` entre as três tabelas
- `agregacoes.py`: `SUM`, `GROUP BY` e `ORDER BY` (total por cliente e pratos mais vendidos)
- `filtros.py`: `COUNT`, `WHERE` e `HAVING`

## Decisões técnicas

- **Preço em centavos (inteiro):** guardo 3800 em vez de 38.0 porque número decimal pode dar erro de arredondamento em contas com dinheiro. Só converto para reais na hora de mostrar.
- **Classe `Pedido`:** os dados do pedido (cliente e itens) e as ações sobre ele (adicionar item, calcular total, salvar) ficam juntos num lugar só. Assim a regra do pedido não se espalha pelo código e dá para testar sem precisar da API.
- **Total calculado antes de salvar:** se um prato não existe, o erro aparece antes de gravar, então nunca fica um pedido pela metade no banco.
- **400 x 422:** o 422 vem da validação do formato da entrada (o Pydantic recusa, por exemplo, quantidade 0 antes de a minha função rodar). O 400 vem da regra de negócio: a classe `Pedido` levanta um erro quando o prato não existe, e a API o converte em resposta 400. A classe não sabe nada de HTTP.
- **Testes em banco temporário:** os testes criam um banco só para eles, então nunca mexem no `restaurante.db` real e podem rodar quantas vezes quiser.

## Limitações conhecidas

- A criação das tabelas `pedidos` e `itens_pedido` está no `sql_pratica.py`, e não no `banco.py`. O ideal é centralizar o esquema em um só lugar.
- Só há dois endpoints: não é possível consultar, alterar nem cancelar um pedido.
- Não há autenticação.
- Os testes cobrem a classe `Pedido`, mas ainda não os endpoints da API.
- O banco é SQLite em arquivo, adequado para estudo, não para vários acessos simultâneos.

## Arquivos

- `api.py`: a API FastAPI
- `modelos.py`: a classe `Pedido`
- `banco.py`: cria o banco e a tabela de pratos a partir de `cardapio.py`
- `cardapio.py`: dados de origem do cardápio
- `sql_pratica.py`: cria as tabelas de pedidos e insere pedidos de exemplo
- `joins.py`, `agregacoes.py`, `filtros.py`: consultas SQL
- `test_modelos.py`: testes automatizados da classe `Pedido`