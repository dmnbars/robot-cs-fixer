import ast
import robot.parsing.model
from robot.api import Token


RUN_KEYWORDS = 'Run Keywords'
AND_KEYWORD = 'AND'


def _capitalize(name):
    return ' '.join([str.capitalize(word) for word in str.split(name, ' ')])


def _capitalize_run_keywords(node: robot.parsing.model.Statement):
    is_keyword = True
    for token in node.get_tokens(Token.ARGUMENT):
        if is_keyword:
            token.value = _capitalize(token.value)
            is_keyword = False
            continue

        if token.value.upper() == AND_KEYWORD:
            token.value = AND_KEYWORD
            is_keyword = True


def _capitalize_name_with_run_keywords(node: robot.parsing.model.Statement):
    token = node.get_token(Token.NAME)
    token.value = _capitalize(token.value)

    if token.value == RUN_KEYWORDS:
        _capitalize_run_keywords(node)


class KeywordCapitalizer(ast.NodeVisitor):
    def visit_SuiteSetup(self, node: robot.parsing.model.Statement):
        _capitalize_name_with_run_keywords(node)

    def visit_SuiteTeardown(self, node: robot.parsing.model.Statement):
        _capitalize_name_with_run_keywords(node)

    def visit_TestSetup(self, node: robot.parsing.model.Statement):
        _capitalize_name_with_run_keywords(node)

    def visit_TestTeardown(self, node: robot.parsing.model.Statement):
        _capitalize_name_with_run_keywords(node)

    def visit_TestCaseName(self, node):
        token = node.get_token(Token.TESTCASE_NAME)
        token.value = _capitalize(token.value)

    def visit_KeywordName(self, node):
        token = node.get_token(Token.KEYWORD_NAME)
        token.value = _capitalize(token.value)

    def visit_KeywordCall(self, node):
        token = node.get_token(Token.KEYWORD)
        token.value = _capitalize(token.value)
