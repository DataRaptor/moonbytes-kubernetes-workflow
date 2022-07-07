import os

templates_path: os.path = os.path.join(
    'kubernetes',
    'templates'
)

values_path: os.path = os.path.join(
    'kubernetes',
    'values.yaml'
)

def get_app_version() -> str:
    with open(values_path, 'r') as f:
        for line in f.readlines():
            if "APP_VERSION" in line:
                return line.split(": ")[-1]
    raise Exception("Could not find APP_VERSION")

if __name__ == '__main__':
    
    app_version: str = get_app_version()

    for template in os.listdir(templates_path):
        template_path: os.path = os.path.join(
            templates_path,
            template)
        lines = []
        with open(template_path, 'r') as f:
            for line in f.readlines():
                if '{{ .Values.APP_VERSION }}' in line:
                    line = line.replace('{{ .Values.APP_VERSION }}', app_version)
                lines.append(line)
        with open(template_path, 'w') as f:
            for line in lines:
                f.writelines(line)
