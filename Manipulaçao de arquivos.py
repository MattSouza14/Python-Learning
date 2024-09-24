senha = 123456
arquivo = open("loginArquivo.txt", "w")
for i in range(51):
    
    if i < 10:
        login ="Sandro00" + str(i)
    elif i <100:
        login ="Sandro0" + str(i)
    else:
        login = "Sandro" + str(i)
    arquivo.write(f"{login}\t {senha}\n")
arquivo.close()

arquivo = open("loginArquivo.txt", "r")
texto = arquivo.read()
print(texto)


loguins = texto.split("\n")
loguins.pop()
lista_cod = []
for login in loguins:
  dado = login.split("\t")
  dado[0] = dado[0].strip()
  cod = int(dado[0][6:])
  lista_cod.append(cod)

print(lista_cod)
ult = max(lista_cod)


arquivo = open("loginArquivo.txt", "a")

for i in range(ult+1, ult+51, 1):
  if i < 10:
    login = "sandro00"+str(i)
  elif i < 100:
    login = "sandro0"+str(i)
  else:
    login = "sandro"+str(i)
  arquivo.write(f"{login} \t {senha}\n")
arquivo.close()

# lista = []

# with open('loginArquivo.txt', 'r') as arquivo:
#     for linha in arquivo:
#         lista.append(linha.strip())

# print(lista[2:9])
# tamanho = len(texto)
# for linha in texto.splitlines():
#     if linha.endswith("50"):  # Verifica se a linha termina com "50"
#         print(linha)
