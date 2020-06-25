import ast

from robot.api import Token


def simple_capitalize(name):
    return ' '.join([str.capitalize(word) for word in str.split(name, ' ')])


def first_letter_to_upper(string):
    return "%s%s" % (str.upper(string[:1]), string[1:])


def only_first_capitalizer(name):
    return ' '.join([first_letter_to_upper(word) for word in str.split(name, ' ')])


SIMPLE_STRATEGY = 'simple'
ONLY_FIRST_STRATEGY = 'only first'
STRATEGIES = (SIMPLE_STRATEGY, ONLY_FIRST_STRATEGY)


class KeywordCapitalizer(ast.NodeVisitor):
    def __init__(self, strategy):
        if strategy not in STRATEGIES:
            raise Exception('unknown capitalize strategy: %s' % strategy)

        if strategy == SIMPLE_STRATEGY:
            self.capitalizer = simple_capitalize

        if strategy == ONLY_FIRST_STRATEGY:
            self.capitalizer = only_first_capitalizer

    def visit_KeywordName(self, node):
        token = node.get_token(Token.KEYWORD_NAME)
        token.value = self.capitalizer(token.value)

    def visit_KeywordCall(self, node):
        token = node.get_token(Token.KEYWORD)
        token.value = self.capitalizer(token.value)
