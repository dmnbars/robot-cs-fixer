import ast

from robot.api import Token


def simple_capitalize(name):
    return ' '.join([str.capitalize(word) for word in str.split(name, ' ')])


def first_letter_to_upper(string):
    return "%s%s" % (str.upper(string[:1]), string[1:])


def only_first_capitalizer(name):
    return ' '.join([first_letter_to_upper(word) for word in str.split(name, ' ')])


class KeywordCapitalizer(ast.NodeVisitor):
    def visit_KeywordName(self, node):
        token = node.get_token(Token.KEYWORD_NAME)
        token.value = simple_capitalize(token.value)

    def visit_KeywordCall(self, node):
        token = node.get_token(Token.KEYWORD)
        token.value = simple_capitalize(token.value)
