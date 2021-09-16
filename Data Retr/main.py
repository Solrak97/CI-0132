# ------------------------------------------------------------
# xmlex.py
#
# tokenizer for an xml subset
# 
# ------------------------------------------------------------


from Parser.xmlex import lexer
from Parser.xmlparser import parser


PATH = 'data.xml'

# Test it out
data = ''
with open(PATH, mode='r', encoding='utf-8') as file:
  data = file.read()
 
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      
     print(tok)


#Reiniciamos el contador de lineas para dar con el error en parser
lexer.lineno = 1

#
s = data # Using predefined data for lex
parser.parse(s)