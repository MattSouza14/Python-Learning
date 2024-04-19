#Tomada de decisão 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("O usuário " + nome + " já pode se alistar")
else:
    print("O usuário " + nome + " não pode se alistar")


gravidadeDoenca = int(input("Digite a gravidade da doença [1-5] "))   

if gravidadeDoenca == 1 | gravidadeDoenca == 2:
    print ("Voce recebera a pulseira Verde")
elif gravidadeDoenca == 3:
    print ("Voce recebera a pulseira Amarela")
elif gravidadeDoenca == 4:
    print ("Voce recebera a pulseira Laranja")
else:
    print ("Voce recebera a pulseira Vermelha")




