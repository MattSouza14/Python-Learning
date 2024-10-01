import csv
dados =[
    ["Nome","Idade","Cidade"],
    ["João", "25", "São Paulo"],
    ["Mateus", "24", "Fortaleza"],
    ["Jorge", "35", "Rio de Janeiro"]
    ]

with open("dados_off.csv", "w", newline="", encoding="latin-1") as arquivo_off:
  escritor_off = csv.writer(arquivo_off, delimiter=";")
  escritor_off.writerows(dados)

with open("dados_off.csv", "r", encoding="latin-1") as arquivo_off:
  leitor_off = csv.reader(arquivo_off, delimiter=";")
  #print(leitor_off)
  for linha in leitor_off:
    print(linha)

with open("dados_on.csv", "r", encoding="utf-8") as arquivo_on:
  leitor_on = list(csv.reader(arquivo_on, delimiter=","))
  print(leitor_on)

for linha in leitor_on:
  if linha[0] == "João":
    linha[1] = 35

with open("dados_on.csv", "w", newline="", encoding="utf-8") as arquivo_on:
  escritor_on = csv.writer(arquivo_on, delimiter=",")
  escritor_on.writerows(leitor_on)
