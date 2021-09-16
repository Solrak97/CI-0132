# ------------------------------------------------------------
 # xmlex.py
 #
 # tokenizer for an xml subset
 # 
 # ------------------------------------------------------------
import ply.lex as lex

'''
Por facilidad de pruebas se toma el archivo desde acá, eventualmente esto se 
puede pasar como parametro en la CLI o una interfaz grafica
'''
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

 'TEXT',
 'URL',
 'DATE',
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
t_RECORD_CLOSE = r'</record>'
t_RECORDS_OPEN = r'<records>'
t_RECORDS_CLOSE = r'</records>'
t_REGION_OPEN = r'<region>'
t_REGION_CLOSE = r'</region>'
t_IDATE_OPEN = r'<initial-date>'
t_IDATE_CLOSE = r'</initial-date>'
t_FDATE_OPEN = r'<final-date>'
t_FDATE_CLOSE = r'</final-date>'
t_NUMBER_OF_VISITS_OPEN = r'<number-of-visits>'
t_NUMBER_OF_VISITS_CLOSE = r'</number-of-visits>'



# DATA REGEX

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
#Corregir años para limitarlo
#Corregir dias y meses para empezar en 1 y no en 0, debe ser la costumbre

#Fix sobre date, cambiar precedencia entre date y text
def t_DATE(t):
     r'(((0[1-9]|1[0-9]|2[0-9]|3[01])-(01|03|05|07|08|10|12))|((0[1-9]|1[0-9]|2[0-9]|30)-(04|06|09|11))|((0[1-9]|1[0-9]|2[0-9])-02))-((19[7-9][0-9])|(2[0-9]{3}))'
     return t

def t_NUMBER_OF_VISITS(t):
     r'(?<=<number-of-visits>)[0-9]+(\.[0-9]+)?(?=</number-of-visits>)'
     return t
   
def t_URL(t):
     r'((https?):\/\/)?(www.)?[a-zA-Z0-9_\-\.]{2,256}\.[a-z]{2,6}(\/([-a-zA-Z0-9@:%._\\+~#?&=]*))*'
     return t

#Añadir soporte para otros lenguajes 
def t_REGION(t):
     r'(?<=<region>)[a-zA-Z ]+(?=</region>)'
     return t

def t_TEXT(t):
     r'[^<>]+'
     return t


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
         break      
#     print(tok)

#Reiniciamos el contador de lineas para dar con el error en parser
lexer.lineno = 1

# Parsing rules
def p_data(t):
    'data : DATA_OPEN topic_collection sites_collection DATA_CLOSE'
    

def p_sites_collection(t):
    'sites_collection : SITES_OPEN sites SITES_CLOSE'

def p_sites(t):
    '''sites  : sites site
                | site'''


def p_site(t):
    'site : SITE_OPEN url title topic_collection record_collection SITE_CLOSE'


def p_topic_collection(t):
    'topic_collection : TOPICS_OPEN topics TOPICS_CLOSE'


def p_topics(t):
    '''topics  : topics topic
                | topic'''


def p_topic(t):
    'topic : TOPIC_OPEN TEXT TOPIC_CLOSE'

    
def p_url(t):
    'url : URL_OPEN URL URL_CLOSE'


def p_title(t):
    'title : TITLE_OPEN TEXT TITLE_CLOSE'


def p_record_collection(t):
    'record_collection : RECORDS_OPEN records RECORDS_CLOSE'


def p_records(t):
    '''records  : records record
                | record'''


def p_record(t):
    'record : RECORD_OPEN idate fdate region numvisits RECORD_CLOSE'

    
def p_idate(t):
    'idate : IDATE_OPEN DATE IDATE_CLOSE'


def p_fdate(t):
    'fdate : FDATE_OPEN DATE FDATE_CLOSE'


def p_region(t):
    'region : REGION_OPEN REGION REGION_CLOSE'


def p_numvisits(t):
    'numvisits : NUMBER_OF_VISITS_OPEN NUMBER_OF_VISITS NUMBER_OF_VISITS_CLOSE'


def p_error(t):
    print(f"Syntax error in line {t.lineno} at {t.value}") 
    exit(0)


import ply.yacc as yacc
parser = yacc.yacc()
s = data # Using predefined data for lex
parser.parse(s)
