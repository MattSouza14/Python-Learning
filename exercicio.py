def tabela_produtos():
    produtos = {
    '001':['teclado', 100.00],
    '002':['mouse', 50.00],
    '003':['monitor', 200.00],
    '004':['impressora', 300.00],
    '005':['scanner', 400.00]
    }
    print("-"*34)
    print("-------CATALOGO DE PRODUTOS-------")
    print("-"*34)
    for key, value in produtos.items():
        print(f"{key}- {value[0]}\t-\tR${value[1]:.2f}")
  

def tabela_desconto():
    forma_pagamento = {
        1: ['avista_dinheiro_cheque', 0.10],
        2: ['avista_cartao', 0.05],
        3: ['duas_vezes', 1],
        4: ['tres_vezes', 1.10]
    }

    for chave, valor in forma_pagamento.items():
        print(f"{chave} - {valor[0]} -> {(valor[1]) * 100:.2f}%")
    

def mostrar_valor():

    pass

def carrinho():
    opcao_produto = input("Digite o codigo do produto desejado: ")

    mostrar_valor()
    pass

def calcular_desconto(pagamento):
    pass

def calcular_parcela():
    pass


def gerar_cupom():
    pass
while True:
    nome = input("Digite seu nome: ")
    tabela_produtos()
    carrinho()
    tabela_desconto()
    formaPagamento = int(input("Digite a forma de pagamento:   "))
    calcular_desconto(formaPagamento)
    calcular_parcela()
    gerar_cupom()
