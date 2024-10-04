language_translation = {
    'dockerfile': 'docker'
}

def language_render_function(x) :
    if x['language'] == None:
        return "-"
    
    y = x['language'].lower()
    y = language_translation[y] if y in language_translation else y
    return f'<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{y}/{y}-plain.svg" alt="{y}-icon" style="width: 28px; height: 28px;" />'

columns = [
    {
        "name": "name",
        "alignment": "",
        "display-name": "Nome do Repositório",
        "render-func": lambda x: f"[{x['name']}](https://github.com/jerobas/{x['name']})"
    },
    {
        "name": "description",
        "alignment": "",
        "display-name": "Descrição",
        "render-func": lambda x: x['description']
    },
    {
        "name": "language",
        "alignment": "center",
        "display-name": "Linguagem Principal",
        "render-func": language_render_function
    },
    {
        "name": "pipeline",
        "alignment": "",
        "display-name": "CI/CD",
        "render-func": lambda x: f'![CI/CD Status](https://img.shields.io/github/actions/workflow/status/jerobas/{x['name']}/release.yml?branch={x['default_branch']})'
    }
]

def stringify_table(repos):
    table_header = ""
    table_size = "|\n"
    table_content = "|\n"

    for column in columns:
        table_header += f"| {column["display-name"]} "
        table_size += f"| {(':' if column['alignment'] == 'center' else '')+(3*'-')+(':' if column['alignment'] == 'center' else '')} "

    for repo in repos:
        line = "|"
        for column in columns:
            line += f" {column['render-func']((repo))} |"
        table_content += line + '\n'
    
    return table_header + table_size + table_content

def md_template(repos):
    template_string = ''
    with open('../.github/profile/template.md', 'r') as f:
        string = stringify_table(repos)
        template_string = f.read()  # Read the template   
        template_string = template_string.replace("[//]: # (table goes here)", string)
    return template_string