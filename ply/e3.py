import ply.lex as lex

# Ejericio 3 – Comentarios

# 1. Compentario de una linea

# 2a. Comentario multilinea completo

# 2b. Comentario multilinea con estados

tokens = (
     'ONE_LINE_COMMENT',
     'MULTI_LINE_COMMENT',
     'NAME',
     'ASSIGN',
     'NUMBER'
)

states = (
    ('comment', 'exclusive'),
)

t_ONE_LINE_COMMENT = r'\#.*'
t_MULTI_LINE_COMMENT = r'"""[\s\S]*?"""'
t_NAME = r'[a-zA-Z][a-zA-Z0-9_]*'
t_ASSIGN = r'='
t_NUMBER = r'\d+'

# def t_MULTI_LINE_COMMENT(t):
#     r'"""'
#     t.lexer.begin('comment')

# def t_comment_MULTI_LINE_COMMENT(t):
#     r'"""'
#     t.lexer.begin('INITIAL')

# def t_comment_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_comment_error(t):
#     t.lexer.skip(1)

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

file = open("input", "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)