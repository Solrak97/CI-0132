# ------------------------------------------------------------
# xmlparser.py
#
# generador de objetos a partir de un subset xml
# 
# ------------------------------------------------------------

from .ply import yacc as yacc
from .xmlex import tokens
from .Structure import *

def item_listing(t):
    if(len(t) == 2):
        t[0] = ListWrapper()
        t[0].add_item(t[1])
    elif(len(t) == 3):
        t[0] = t[1].add_item(t[2])

doc_data = {}

def p_data(t):
    'data : DATA_OPEN topic_collection sites_collection DATA_CLOSE'
    global doc_data
    doc_data = Data(t[2].items, t[3].items)
    t[0] = Data(t[2].items, t[3].items)
    pass


def p_sites_collection(t):
    'sites_collection : SITES_OPEN sites SITES_CLOSE'
    t[0] = t[2]
    pass


def p_sites(t):
    '''sites  : sites site
                | site'''
    item_listing(t)
    pass


def p_site(t):
    'site : SITE_OPEN url title topic_collection record_collection SITE_CLOSE'
    t[0] = Site(t[2], t[3], t[4].items, t[5].items)
    pass




def p_topic_collection(t):
    'topic_collection : TOPICS_OPEN topics TOPICS_CLOSE'
    t[0] = t[2]
    pass


def p_topics(t):
    '''topics  : topics topic
                | topic'''
    item_listing(t)
    pass


def p_topic(t):
    'topic : TOPIC_OPEN TEXT TOPIC_CLOSE'
    t[0] = t[2]
    pass

    
def p_url(t):
    'url : URL_OPEN URL URL_CLOSE'
    t[0] = t[2]
    pass


def p_title(t):
    'title : TITLE_OPEN TEXT TITLE_CLOSE'
    t[0] = t[2]
    pass


def p_record_collection(t):
    'record_collection : RECORDS_OPEN records RECORDS_CLOSE'
    t[0] = t[2]
    pass


def p_records(t):
    '''records  : records record
                | record'''
    item_listing(t)
    pass


def p_record(t):
    'record : RECORD_OPEN idate fdate region numvisits RECORD_CLOSE'
    t[0] = Record(t[2], t[3], t[4], t[5])
    pass

    
def p_idate(t):
    'idate : IDATE_OPEN DATE IDATE_CLOSE'
    t[0] = t[2]
    pass


def p_fdate(t):
    'fdate : FDATE_OPEN DATE FDATE_CLOSE'
    t[0] = t[2]
    pass


def p_region(t):
    'region : REGION_OPEN REGION REGION_CLOSE'
    t[0] = t[2]
    pass


def p_numvisits(t):
    'numvisits : NUMBER_OF_VISITS_OPEN NUMBER_OF_VISITS NUMBER_OF_VISITS_CLOSE'
    t[0] = t[2]
    pass


def p_error(t):
    print(f"Syntax error in line {t.lineno} at {t.value}") 
    pass




parser = yacc.yacc()