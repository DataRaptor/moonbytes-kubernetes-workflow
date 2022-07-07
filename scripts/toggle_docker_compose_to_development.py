import os

docker_compose_path: os.path = os.path.join(
    'docker-compose.yaml' 
)


def toggle_docker_compose_to_development():
    lines = []
    with open(docker_compose_path, 'r') as f:
        for line in f.readlines():
            if 'image' in line and 'gcr.io' in line:
                if not '#' in line:
                    line = "#{}".format(line)
            lines.append(line)
    with open(docker_compose_path, 'w') as f:
        for line in lines:
            f.writelines(line)

toggle_docker_compose_to_development()