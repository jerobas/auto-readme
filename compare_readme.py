import os
import requests
from dotenv import load_dotenv
from md_template import md_template

load_dotenv()
github_token = os.getenv('GITHUB_TOKEN')

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

# response = requests.get("https://api.github.com/orgs/jerobas/repos", headers={'authorization': f'{github_token}'})
# repos = response.json()
    
# string = md_template(repos)

# with open("../.github/profile/readme.md", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
#     output_file.write(string)