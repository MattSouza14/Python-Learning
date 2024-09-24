#Variaveis
#Tipos de dados
name = "Mateus"
age = 24
saldoConta = 151.20
userAtivo = True

#Checar o tipo de variavel
#type(nomeDaVariavel)
print ("O tipo de dado da variavel [name]: ", type(name))
print ("O tipo de dado da variavel [age]: ", type(age))
print ("O tipo de dado da variavel [saldoConta]: ", type(saldoConta))
print ("O tipo de dado da variavel [userAtivo]: ", type(userAtivo))

#Atribuição multipla
a = b = c = 10
print(a, b, c)
#Entrada de dados
m, a, t = input("Digite um num: "), input("Digite outro num: "), input("Digite mais um num: ")
print(m, a, t)

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

# Igual a (==): devolve True se ambos os valores são iguais.
# Diferente de (!=): devolve True se os valores são diferentes.
# Maior que (>): devolve True se o primeiro valor é maior que o segundo.
# Menor que (<): devolve True se o primeiro valor é menor que o segundo.
# Maior ou igual que (>=): devolve True se o primeiro valor é maior ou igual que o segundo.
# Menor ou igual que (<=): devolve True se o primeiro valor é menor ou igual que o segundo.

# AND (and): devolve True se ambas as condições são verdadeiras.
# OR (or): devolve True se ao menos uma das condições é verdadeira.
# NOT (not): inverte o valor de uma condição, devolve True se a condição é falsa e False se a 
# condição é verdadeira.

print(soma, mult, div, resto, pot)
print("Soma: ", format(soma))
print(f"Subtração: {sub}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Resto: {resto}")
print(f"Potência: {pot}")
print(pow(x, 3))

#Metodos para strings
# split(",")
# lower()
# upper()
# capitalize()
#title()
#find("@gmail.com")
#replace(",", ".")
#strip()