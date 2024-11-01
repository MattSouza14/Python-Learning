import instaloader

def ColetarSeguidores(nomeUsuario, senha, nomeDePerfil):
    insta = instaloader.Instaloader()
    insta.login(nomeUsuario, senha)

    profile = instaloader.Profile.from_username(insta.context, nomeDePerfil)

    seguidores = []
    for seguidor in profile.get_followers:
        seguidores.append({
            "id": seguidor.id,
            "Nome de usuario": seguidor.username,
        })
    return seguidores
