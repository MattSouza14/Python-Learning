#Foor
# O loop for é utilizado para iterar sobre uma sequência 
# (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável.

# for variável in sequência:
    #Bloco de código a repetir
    #instruções

frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

#While
#O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.

#while condição:

    # Bloco de código a repetir
    #instruções


contador = 0

while contador < 5:

    print(contador)
    contador += 1

#Controle de loops
# [Break]
# A instrução break é utilizada para sair prematuramente de um loop, 
# independentemente da condição. Quando um break é encontrado, o loop é interrompido 
# e o fluxo de execução continua com a próxima instrução fora do loop.

cont = 0
while True:

    print(cont)
    cont += 1
    if cont == 5:
        break

# [Continue]
# A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop 
# e passar para a próxima iteração.

for i in range(2,15):

    if i % 2 == 0:
        continue
    print(i)

# [Pass]
# A instrução pass é uma operação nula que não faz nada. 
# É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, 
# mas nenhuma ação é desejada.

for i in range(5):
    pass