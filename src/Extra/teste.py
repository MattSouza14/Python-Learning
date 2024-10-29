import instaloader

perfis = ["code._learning", "selenium_webdriver_java", "aacoding_tips", "web_development_legend"]

insta = instaloader.Instaloader()

for perfil in perfis:
    insta.download_profile(perfil, profile_pic=True)
    profile = instaloader.Profile.from_username(insta.context, perfil)
    print(f"Nome: {profile.full_name}")
    print(f"Seguidores: {profile.followers}")  
