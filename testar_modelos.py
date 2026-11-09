from modelos import Pedido

pedido = Pedido("Diego")
pedido.adicionar_item(1, 2)
pedido.adicionar_item(4)

print("Total:", pedido.total_centavos())
print("Salvo com id:", pedido.salvar())

try:
    pedido.adicionar_item(99)
    pedido.total_centavos()
except ValueError as erro:
    print("Erro:", erro)