usuarios = {}
print(usuarios)
usuarios ={
    "mateus" : ["Mateus Souza", "11/05/2024", "Recep_01"],
    "carlos" : ["Carlos Souza", "03/02/2023", "Recep_02"]
}
print(usuarios)

usuarios["felipe"] = ["Felipe Souza", "11/05/2024", "Raiox_01"]#Adicionando na lista

print(usuarios)

print("######-----######")
print(usuarios.get("mateus"))#get pega um valor especifico do dicionario
