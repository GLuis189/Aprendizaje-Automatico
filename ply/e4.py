import ply.lex as lex

# Ejercicio 4 – Palabras reservadas

# 1. Definir palabras reservadas.

# 2. Definir tokens, incluyendo palabras reservadas.

# 3. Crear reserved map.

# 4. Usar reserved map en la definición de t_ID.

reserved = (
    "VAR",
    "WHILE"
)

tokens = (
    "LBRACKET",
    "RBRACKET",
    "ID",
    "NUMBER",
    "LT",
    "LE",
    "GT"
) + tuple(reserved)

t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LT = r"{"
t_LE = r"="
t_GT = r"}"
t_NUMBER = r"\d+"

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r


t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved_map.get(t.value, "ID")
    return t

lexer = lex.lex()

file = open("input4", "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)