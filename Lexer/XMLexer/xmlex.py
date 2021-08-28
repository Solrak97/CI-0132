# ------------------------------------------------------------
 # xmlex.py
 #
 # tokenizer for an xml subset
 # 
 # ------------------------------------------------------------
import ply.lex as lex


PATH = 'data.xml'

'''
data
topics
topic
sites
site
url
title
record
region
initial-date
final-date 
number-of-visits 
'''


tokens = (  

# TAGS

 'DATA_OPEN', 
 'DATA_CLOSE',
 'TOPIC_OPEN',
 'TOPIC_CLOSE',
 'TOPICS_OPEN',
 'TOPICS_CLOSE',
 'SITE_OPEN',
 'SITE_CLOSE',
 'SITES_OPEN',
 'SITES_CLOSE',
 'URL_OPEN',
 'URL_CLOSE',
 'TITLE_OPEN',
 'TITLE_CLOSE',
 'RECORD_OPEN',
 'RECORD_CLOSE',
 'RECORDS_OPEN',
 'RECORDS_CLOSE',
 'REGION_OPEN',
 'REGION_CLOSE',
 'IDATE_OPEN',
 'IDATE_CLOSE',
 'FDATE_OPEN',
 'FDATE_CLOSE',
 'NUMBER_OF_VISITS_OPEN',
 'NUMBER_OF_VISITS_CLOSE',


# TEXTOS

 'TOPIC_TEXT',
 'URL_TEXT',
 'TITLE_TEXT',
 'IDATE',
 'FDATE',
 'REGION',
 'NUMBER_OF_VISITS',
)


# TAG REGEX

t_DATA_OPEN = r'<data>'
t_DATA_CLOSE = r'</data>'
t_TOPIC_OPEN = r'<topic>'
t_TOPIC_CLOSE = r'</topic>'
t_TOPICS_OPEN = r'<topics>'
t_TOPICS_CLOSE = r'</topics>'
t_SITE_OPEN = r'<site>'
t_SITE_CLOSE = r'</site>'
t_SITES_OPEN =  r'<sites>'
t_SITES_CLOSE = r'</sites>'
t_URL_OPEN = r'<url>'
t_URL_CLOSE = r'</url>'
t_TITLE_OPEN = r'<title>'
t_TITLE_CLOSE = r'</title>'
t_RECORD_OPEN = r'<record>'
t_RECORDS_CLOSE = r'</record>'
t_RECORDS_OPEN = r'<records>'
t_RECORD_CLOSE = r'</records>'
t_REGION_OPEN = r'<region>'
t_REGION_CLOSE = r'</region>'
t_IDATE_OPEN = r'<initial-date>'
t_IDATE_CLOSE = r'</initial-date>'
t_FDATE_OPEN = r'<final-date>'
t_FDATE_CLOSE = r'</final-date>'
t_NUMBER_OF_VISITS_OPEN = r'<number-of-visits>'
t_NUMBER_OF_VISITS_CLOSE = r'</number-of-visits>'



# DATA REGEX

t_TOPIC_TEXT = r'(?<=<topic>)[\w ]+(?=</topic>)'
t_URL_TEXT = r'(?<=<url>)https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)(?=</url>)'
t_TITLE_TEXT = r'(?<=<title>)[\w ]+(?=</title>)'
t_IDATE = r'(?<=<initial-date>)([0-2][0-9]|[3][0-1])-([0][0-9]|1[0-9])-([0-9]){4}(?=</initial-date>)'
t_FDATE = r'(?<=<final-date>)([0-2][0-9]|[3][0-1])-([0][0-9]|1[0-9])-([0-9]){4}(?=</final-date>)'
t_REGION = r'(?<=<region>)[\w ]+(?=</region>)'
t_NUMBER_OF_VISITS = r'(?<=<number-of-visits>)[0-9]+.?[0-9]*(?=</number-of-visits>)'





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
  data = file.read()
 
# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)