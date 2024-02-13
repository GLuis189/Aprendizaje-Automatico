import ply.lex as lex

# Ejercicio 4 – Palabras reservadas

# 1. Definir palabras reservadas.

# 2. Definir tokens, incluyendo palabras reservadas.

# 3. Crear reserved map.

# 4. Usar reserved map en la definición de t_ID.

tokens = (
    "INTEGER",
    "FLOAT"
)

def t_FLOAT(t):
    r"(\d+\.\d+)|(\.\d+)"
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

file = open("input5", "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)