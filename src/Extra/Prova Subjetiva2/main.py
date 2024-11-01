# import instaloader
from ColetarDados import * 

nomeDoUsuarioLogin = input("Digite seu nome de usuario: ")
senhaDoUsuarioLogin= input("Digite sua senha: ")
perfilPesquisado = input("Digite o nome de perfil a ser pesquisado: ")

dadosDaConta = ColetarSeguidores(nomeDoUsuarioLogin, senhaDoUsuarioLogin, perfilPesquisado)