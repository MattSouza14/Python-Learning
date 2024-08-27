#Variaveis
name = input("Digite seu nome: ")#Função input armazena o valor dado pelo usuário 
print ("Bem vindo " + name)
age = int(input("Digite sua idade: "))#Função int usado junto com input para saber que é uma string e o py vai usar como numero inteiro
print ("Voce tem ", age)
saldoConta = float(input("Digite seu saldo atual na conta: "))
print ("Seu saldo é: R$", saldoConta)
# ou
print(f"Seu saldo é: R${saldoConta}")

m, a, t = input("Digite um num: "), input("Digite outro num: "), input("Digite mais um num: ")
print(m, a, t)

#Checar o tipo de variavel
#type(nomeDaVariavel)
print ("O tipo de dado da variavel [name]: ", type(name))
print ("O tipo de dado da variavel [age]: ", type(age))
print ("O tipo de dado da variavel [saldoConta]: ", type(saldoConta))

# Operadores
x = 5
# soma
soma = x + 5
# subtração
sub = x - 3
# multiplicação
mult = x * 2
# divisão 
div = x / 2
# módulo ou resto da divisão
resto = x % 3
# potência
pot = x ** 2

print(soma, sum, mult, div, resto, pot)
print("Soma: ", format(soma))
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Resto: {resto}")
print(f"Potência: {pot}")
print(pow(x, 3))

# split(",")
# lower()
# upper()
# capitalize()
#title()
#find("@gmail.com")