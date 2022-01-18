import os
from robot.api import get_model
from formatter.capitalizer import KeywordCapitalizer


def _fix_file(file: str):
    model = get_model(file)
    KeywordCapitalizer().visit(model)
    model.save()


class Fixer:
    def __init__(self, paths: list):
        self._paths = paths

    def _get_files(self):
        for path in self._paths:
            if os.path.isfile(path):
                yield path
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.robot'):
                        yield root + os.sep + file

    def fix(self):
        for path in self._get_files():
            _fix_file(path)
