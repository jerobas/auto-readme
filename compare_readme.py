import requests
from md_template import md_template

response = requests.get("https://api.github.com/orgs/jerobas/repos", headers={'authorization': ''})
repos = response.json()

for i in repos:
    print(i['default_branch'])
    
string = md_template(repos)

with open("../.github/profile/readme.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(string)