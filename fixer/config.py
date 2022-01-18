import os


class Config:
    def __init__(self, paths: list):
        self._paths = paths

    def get_files(self):
        for path in self._paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.robot'):
                        yield os.path.realpath(root + os.sep + file)
