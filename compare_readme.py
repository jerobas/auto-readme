import os
import requests
from dotenv import load_dotenv
from md_template import md_template

load_dotenv()
github_token = os.getenv('GITHUB_TOKEN')

response = requests.get("https://apiglobal-repo/.github.com/orgs/jerobas/repos", headers={'authorization': f'{github_token}'})
repos = response.json()

for i in repos:
    print(i['default_branch'])
    
string = md_template(repos)

with open("../global-repo/.github/profile/readme.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(string)