import ply.lex as lex

# Ejercicio 4 – Palabras reservadas

# 1. Definir palabras reservadas.

# 2. Definir tokens, incluyendo palabras reservadas.

# 3. Crear reserved map.

# 4. Usar reserved map en la definición de t_ID.

tokens = (
    "NOMBRE",
    "DNI",
    "CORREO",
    "CIUDAD",
    "TELEFONO",
    "MATRICULA"
)
t_NOMBRE = r"(\w+\s){2}\w+"
t_DNI = r"\d{8}[A-Z]"
t_CORREO = r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]+"
t_CIUDAD = r"\w+\s(\w+)"
t_TELEFONO = r"\+\d+\s\d{9}"
t_MATRICULA = r"\d{4}\s[A-Z]{3}"


t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

file = open("input6", "r")
lexer.input(file.read())
for token in lexer:
    print(token.type, token.value)