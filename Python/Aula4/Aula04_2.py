#funções
def perguntar(): 
    return  input("Escolha um opção\n" +
              "<I> - Para inserir um usuario\n" +
              "<P> - Para pesquisar um usuario\n" +
              "<E> - Para excluir um usuario\n" +
              "<L> - Para listar um usuario: ").upper()
def inserir(dicionario):
    dicionario [input("Digite o login: ").upper()]= [input("Digite o nome: ").upper(), 
                                                   input("Digite a ultima data de acesso: "), 
                                                   input("Qual a ultima estação acessada: ").upper()]
##########################################################################################################

users = []

opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
       inserir(users)
    opcao = perguntar()