import os


class Config:
    def __init__(self, paths: list, rules: dict):
        self._paths = paths
        self.rules = rules

    def _validate(self):
        pass

    def get_files(self):
        for path in self._paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.robot'):
                        yield os.path.realpath(root + os.sep + file)
