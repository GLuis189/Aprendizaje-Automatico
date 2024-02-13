import ply.lex as lex
import sys

# la variable siempre tiene que llamarse así
tokens = (
    "PALABRA",
    "NUMERO"
)

# empuerza en t_
t_PALABRA = r'[a-zA-Z][a-zA-Z0-9_]*'

# type valor linenumber lexcol
def t_NUMERO(token):
    r'[1-9][0-9]*'
    token.value = int(token.value)
    return token

t_ignore = r' \t'

def t_newline(token):
    r'\n+'
    print("New line!!", token.lexer.lineno)
    token.lexer.lineno = token.value.count('\n')

def t_error(token):
    print("[EX1][LEXER] Ilegal character:" + token.value)
    token.lexer.skip(1)

lexer = lex.lex()

# con una variable
lexer.input("palabra variable_1 123 32")

"""for token in lexer:
    print(token.type, token.value)
"""    
file = open(sys.argv[1])
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)