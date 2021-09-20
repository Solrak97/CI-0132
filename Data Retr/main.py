# ------------------------------------------------------------
# main.py
#
# Punto de inicio 
# 
# ------------------------------------------------------------


from Parser.xmlex import lexer
from Parser.xmlparser import parser, doc_data
#   Carga del archivo CSV 
PATH = 'data.xml'
data = ''
with open(PATH, mode='r', encoding='utf-8') as file:
    data = file.read()
 

#   Lexing
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok: 
        break      
#    print(tok)


#   Reset del contador
lexer.lineno = 1


#   Se obtiene el objeto padre que contiene la informacion del archivo
data = parser.parse(data)


print(data.to_string())    