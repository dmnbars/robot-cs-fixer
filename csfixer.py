import os
import yaml

from robot.api import get_model

from formatter.capitalizer import KeywordCapitalizer


def find_files(directories):
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.robot'):
                    yield os.path.realpath(root + os.sep + file)


def get_config(config_path):
    cfg = parse_config(config_path)
    if 'dirs' not in cfg:
        raise Exception("'dirs' not provided")
    if 'rules' not in cfg:
        raise Exception("'rules' not provided")

    return cfg


def parse_config(config_path):
    try:
        with open(config_path, 'r') as stream:
            try:
                cfg = yaml.safe_load(stream)
                if not isinstance(cfg, dict):
                    raise Exception("config file can not be parsed")

                return cfg

            except yaml.YAMLError as exc:
                raise Exception("config file can not be parsed: '" + str(exc))

    except IOError:
        raise Exception("config file at '" + config_path + "' not accessible")


def fix(file, rules):
    model = get_model(file)

    if 'capitalize' in rules:
        KeywordCapitalizer(rules['capitalize']).visit(model)

    model.save()


if __name__ == "__main__":
    try:
        config = get_config("csfixer.yaml")

        for path in find_files(config['dirs']):
            fix(path, config['rules'])
    except Exception as e:
        print(f'Error: {e}')
