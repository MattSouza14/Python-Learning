import pandas as pd

produtos = []

res = 'sim'
while res == "sim":
    produto = {}
    produto["codigo"] = input("Digite o código do produto: ")
    produto["nome"] = input("Digite o nome do produto: ")
    produto["preco"] = float(input("Digite o preço do produto: "))
    produto["quant"] = int(input("Digite o estoque do produto: "))
    
    produtos.append(produto)
    
    res = input("Quer cadastrar outro produto? (sim/nao) ").lower().replace("ã","a")

print("\nCODE\tNAME\tVALUE\tQUANT")
for p in produtos:
    print(f"{p['codigo']}\t{p['nome']}\t{p['preco']:.2f}\t{p['quant']}")

with open('relatorioEstoque.txt','w') as arquivo:
    arquivo.write("Code\tNome\tQuant\tPreco \n")
    for p in produtos:
        arquivo.write(f"{p['codigo']}\t{p['nome']}\t{p['quant']}\t{p['preco']}\n")
        

vendasRealizadas = []

resVenda = 'sim'
while resVenda == 'sim':
    print("\nCODE\tNAME\tVALUE\tQUANT")
    for p in produtos:
        print(f"{p['codigo']}\t{p['nome']}\t{p['preco']:.2f}\t{p['quant']}")

    codigoVenda = input("\nDigite o código do produto: ")
    quantidadeVenda = int(input("Digite a quantidade vendida: "))

    for p in produtos:
        if p['codigo'] == codigoVenda:
            if p['quant'] >= quantidadeVenda:
                p['quant'] -= quantidadeVenda
                valorTotal = quantidadeVenda * p['preco']
                vendasRealizadas.append({
                    "code": p['codigo'],
                    "nome": p['nome'],
                    "quant": quantidadeVenda,
                    "valorTotal": valorTotal
                })
                print(f"Venda realizada com sucesso!\nVocê vendeu {quantidadeVenda} unidades do produto {p['nome']}.")
                break
            else:
                print(f"Estoque insuficiente para realizar a venda de {quantidadeVenda} unidades do produto {p['nome']}.")
                break
    else:
        print("Código do produto não encontrado.")
    
    resVenda = input("Quer realizar outra venda? (sim/nao) ").lower()


if vendasRealizadas:
    vendas = pd.DataFrame(vendasRealizadas)
    vendas.to_csv('relatorioVendas.csv', index=False)

    print("\nRelatório gerado")


