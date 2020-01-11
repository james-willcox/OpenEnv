import yaml

file_path = 'config.yml'


def read_config():
    with open(file_path, 'r') as stream:
        return yaml.safe_load(stream)


if __name__ == "__main__":
    file = read_config()
    print(file)
    print(file['app_config']['debug'])
