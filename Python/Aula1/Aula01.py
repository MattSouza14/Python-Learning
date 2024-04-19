#Variaveis
name = input("Digite seu nome: ")#Função input armazena o valor dado pelo usuário 
print ("Bem vindo " + name)
age = int(input("Digite sua idade: "))#Função int usado junto com input para saber que é uma string e o py vai usar como numero inteiro
print ("Voce tem ", age)
saldoConta = float(input("Digite seu saldo atual na conta: "))
print ("Seu saldo é: ", saldoConta, "R$")

#Checar o tipo de variavel
#type(nomeDaVariavel)
print ("O tipo de dado da variavel [name]: ", type(name))
print ("O tipo de dado da variavel [age]: ", type(age))
print ("O tipo de dado da variavel [saldoConta]: ", type(saldoConta))


