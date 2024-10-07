import os
import requests
from dotenv import load_dotenv
from md_template import md_template

load_dotenv()
github_token = os.getenv('PAT_TOKEN')

response = requests.get("https://api.github.com/orgs/jerobas/repos", headers={'authorization': f'{github_token}'})
repos = response.json()

repos = [repo for repo in repos if repo["name"] != ".github"]
repos.sort(key=lambda x: x["name"])

# Loop through each repository and get its workflows
for repo in repos:
    repo_name = repo['name']
    workflows_response = requests.get(
        f"https://api.github.com/repos/jerobas/{repo_name}/actions/workflows",
        headers={'authorization': f'token {github_token}'}
    )
    workflows = workflows_response.json()
    if 'workflows' in workflows:
        repo['pipeline'] = any(workflow['path'] == '.github/workflows/release.yml' for workflow in workflows['workflows'])
    else:
        repo['pipeline'] = False

string = md_template(repos)

with open("../.github/profile/readme.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(string)