import instaloader

loader = instaloader.Instaloader()
 
# loader.login("bizu_java", "km1056c")
loader.login("mattsouzzza", "Newsenha0302")


profile = instaloader.Profile.from_username(loader.context, "mattsouzzza")

followers = profile.get_followers()
for follower in followers:
    print(follower)