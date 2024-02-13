import ply.lex as lex

class lexerClass():
    def __init__(self):
        self.lexer = lex.lex(module=self)

    tokens = (
    "PALABRA",
    "NUMERO"
    )

    t_PLUS = r"\+"
    t_MINUS = r"\-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_EQUAL = r"="

