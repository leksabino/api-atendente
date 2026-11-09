# cardapio.py - Banco de dados oficial de pratos do restaurante

CARDAPIO = [
    {
        "id": 1,
        "nome": "Hambúrguer Artesanal Clássico",
        "categoria": "Lanches",
        "preco": 38.00,
        "tempo_preparo_min": 20,
        "ingredientes": ["pão brioche", "hambúrguer bovino 180g", "queijo cheddar", "bacon"],
        "alergenicos": ["glúten", "lactose"],
        "vegetariano": False,
        "vegano": False
    },
    {
        "id": 2,
        "nome": "Salada Caesar com Frango Crocante",
        "categoria": "Saladas",
        "preco": 36.00,
        "tempo_preparo_min": 15,
        "ingredientes": ["frango 150g", "alface americana", "croutons de pão", "molho caesar"],
        "alergenicos": ["glúten", "lactose"],
        "vegetariano": False,
        "vegano": False
    },
    {
        "id": 3,
        "nome": "Bowl Vegano de Grão de Bico e Abacate",
        "categoria": "Vegano",
        "preco": 34.00,
        "tempo_preparo_min": 15,
        "ingredientes": ["mix de folhas", "grão de bico crocante", "abacate", "tomate cereja"],
        "alergenicos": [],
        "vegetariano": True,
        "vegano": True
    },
    {
        "id": 4,
        "nome": "Suco Natural de Laranja com Morango (500ml)",
        "categoria": "Bebidas",
        "preco": 12.00,
        "tempo_preparo_min": 5,
        "ingredientes": ["laranja fresca", "morango"],
        "alergenicos": [],
        "vegetariano": True,
        "vegano": True
    }
]