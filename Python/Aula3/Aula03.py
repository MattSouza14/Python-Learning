#Laços de repetição- WHILE
#dá uma condição e o codigo será executado até que essa condição seja falsa

numero = int(input("Digite um numero: "))
while numero <= 100:
    print("\t" + str(numero))#str transforma o numero em texto
    numero = numero + 1

print ("Fim do laço")

#Laço de repetição - FOR

tabuada = int(input("Digite o numero da tabuada: "))
print("Tabuada do numero", tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + " X " + str(valor) + " = " + str(tabuada*valor))