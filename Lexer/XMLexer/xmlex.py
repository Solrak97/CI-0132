# ------------------------------------------------------------
 # xmlex.py
 #
 # tokenizer for an xml subset
 # 
 # ------------------------------------------------------------
import ply.lex as lex


PATH = 'data.xml'


# List of token names.   This is always required
tokens = (
    'DATA_B',
    'DATA_E',

    'TOPICS_B',
    'TOPICS_E',
)
 
# Regular expression rules for simple tokens
t_DATA_B = r'<data>'
t_DATA_E = r'</data>'
 
t_TOPICS_B = r'<topics>'
t_TOPICS_E = r'</topics>'


# A regular expression rule with some action code
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t
 
 # Define a rule so we can track line numbers
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()

# Test it out
data = ''
with open(PATH) as file:
     data += file.readline()
 
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)