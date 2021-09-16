# ------------------------------------------------------------
# xmlparser.py
#
# generador de objetos a partir de un subset xml
# 
# ------------------------------------------------------------

from .ply import yacc as yacc
from .xmlex import tokens

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
    print(t[2])

    
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

parser = yacc.yacc()