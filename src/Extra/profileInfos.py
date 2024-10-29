import instaloader
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
perfis = ["code._learning", "selenium_webdriver_java", "web_development_legend", "aacoding_tips"]

insta = instaloader.Instaloader()
# loader = instaloader.Instaloader()
insta.login("bizu_java", "knn1056c")
# name_profile = "julebs_"
# profile =  instaloader.Profile.from_username(insta.context, name_profile)
maxSeguidores = 0
perfilTop = None

for perfil in perfis:
    try:
        profile = instaloader.Profile.from_username(insta.context, perfil)
        print(f"Nome: {profile.full_name} - Seguidores: {profile.followers}")  
        if profile.followers > maxSeguidores:
            maxSeguidores = profile.followers
            perfilTop = profile.full_name
    except Exception as e:
        print(f"Erro ao acessar o perfil {perfil}: {e}")

print(f"TOP PERFIL: {perfilTop} - TOP SEGUIDORES {maxSeguidores}")       





# print(f"Name: {profile.full_name}")
# # print(f"Name: {profile.location}")
# print(f"Biografia: {profile.biography}")
# print(f"Seguindo: {profile.followers}")
# print(f"Seguidores: {profile.followees}")
# print(f"Posts: {profile.mediacount}")



