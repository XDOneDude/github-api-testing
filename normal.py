from github import Github
TOKEN = open("token.txt", "r").read()
username = "your token"
g = Github(TOKEN)
github = g.get_user(username)
REPOS = [ _ for _ in github.get_repos()]
print(REPOS)