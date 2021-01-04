from fixer.config import Config
from robot.api import get_model
from formatter.capitalizer import KeywordCapitalizer


class Fixer:
    def __init__(self, config: Config):
        self.config = config

    def fix(self):
        for path in self.config.get_files():
            self._fix_file(path)

    def _fix_file(self, file: str):
        model = get_model(file)

        if 'capitalize' in self.config.rules:
            KeywordCapitalizer(self.config.rules['capitalize']).visit(model)

        model.save()
