import hashlib
# import csv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import serialization, hashes


chavePrivada = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

chavePublica = chavePrivada.public_key()
print(chavePrivada)
print(chavePublica)

msg= "ola carai"
msgCifrada = chavePublica.encrypt(
    msg,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA3_256(),
        label= None
    )
)
print(msgCifrada)

msgDescriptorafada = chavePrivada.decrypt(
    msgCifrada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA3_256(),
        label= None
    )
)

#Gerar uma chave de criptografia simetrica
chave = Fernet.generate_key()
print(chave)

fernet = Fernet(chave)
mensagem = b"Ola mundo"
mensagemCifrada = fernet.encrypt(mensagem)
print(mensagemCifrada)


mensagemDescript= fernet.decrypt(mensagemCifrada)
print(mensagemDescript)

#CRIAR ARQUIVO E GERAR A HAS
arquivo = open("teste.txt", "w")
arquivo.write("Texto para hash")
arquivo.close()

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    hash_arquivo = hashlib.sha256(conteudo.encode('utf-8'))
    has_hex = hash_arquivo.hexdigest()
    print(has_hex)

#EDITAR ARQUIVO
arquivo2 = open("teste.txt", "w")
arquivo2.write("Texto para hashhh")
arquivo2.close()

# with open ("teste.txt", 'a') as arquivo2:
#     arquivo2.write("Texto para hash2")
#     arquivo2.close()

with open("teste.txt", "r") as arquivo2:
    conteudo2 = arquivo2.read()
    hash_arquivo2 = hashlib.sha256(conteudo2.encode('utf-8'))
    has_hex2 = hash_arquivo2.hexdigest()
    print(has_hex2)

if has_hex == has_hex2:
    print("Arquivo seguro")
else: 
    print("Arquivo alterado")

def criptoSenha(senha):
    senhaCorreta = "mattsouza123"
    hash_object = hashlib.sha256(senhaCorreta.encode('utf-8'))
    hash_correto = hashlib.sha256(senha.encode('utf-8'))
    has_hex=hash_object.hexdigest()
    has_certo = hash_correto.hexdigest()
    
    if has_hex == has_certo:
        return  print ("Logado")
    else:
        return print("Senha errada carai")     

    
# texto = "olá mundoooooo"
email=input("Digite seu email ")
senha = input("Digite sua senha ")


retorno = criptoSenha(senha)

print(retorno)              







