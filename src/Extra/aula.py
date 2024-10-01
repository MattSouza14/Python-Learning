produtos = []


res = 'sim'
while res.lower() == "sim":
    produto = {}
    produto["codigo"] = input("Digite o código do produto: ")
    produto["nome"] = input("Digite o nome do produto: ")
    produto["preco"] = float(input("Digite o preço do produto: "))
    produto["quant"] = int(input("Digite o estoque do produto: "))
    
    produtos.append(produto)
    
    res = input("Quer cadastrar outro produto? (sim/não) ").lower()

print("\nCODE\tNAME\tVALUE\tQUANT")
for p in produtos:
    print(f"{p['codigo']}\t{p['nome']}\t{p['preco']:.2f}\t{p['quant']}")
    # print(f"Valor total do estoque {p['preco'] * p['quant']}")

resVenda = 'sim'
while resVenda == 'sim':
    for p in produtos:
        print("pr")
        print("\nCODE\tNAME\tVALUE\tQUANT")
        print(f"{p['codigo']}\t{p['nome']}\t{p['preco']:.2f}\t{p['quant']}")
    codigoVenda = input("\nDigite o código do produto: ")
    quantidadeVenda = int(input("Digite a quantidade vendida: "))

    for p in produtos:
        if p['codigo'] == codigoVenda:
            if p['quant'] >= quantidadeVenda:
                p['quant'] -= quantidadeVenda
                print(f"Venda realizada com sucesso!\nVocê vendeu {quantidadeVenda} unidades do produto {p['nome']}.")
                break
            else:
                print(f"Estoque insuficiente para realizar a venda de {quantidadeVenda} unidades do produto {p['nome']}.")
                break
    else:
        print("Código do produto não encontrado.")
    
    resVenda = input("Quer realizar outra venda? (sim/não) ").lower()


