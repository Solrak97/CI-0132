
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DATA_CLOSE DATA_OPEN DATE FDATE_CLOSE FDATE_OPEN IDATE_CLOSE IDATE_OPEN NUMBER_OF_VISITS NUMBER_OF_VISITS_CLOSE NUMBER_OF_VISITS_OPEN RECORDS_CLOSE RECORDS_OPEN RECORD_CLOSE RECORD_OPEN REGION REGION_CLOSE REGION_OPEN SITES_CLOSE SITES_OPEN SITE_CLOSE SITE_OPEN TEXT TITLE_CLOSE TITLE_OPEN TOPICS_CLOSE TOPICS_OPEN TOPIC_CLOSE TOPIC_OPEN URL URL_CLOSE URL_OPENdata : DATA_OPEN topic_collection sites_collection DATA_CLOSEsites_collection : SITES_OPEN sites SITES_CLOSEsites  : sites site\n                | sitesite : SITE_OPEN url title topic_collection record_collection SITE_CLOSEtopic_collection : TOPICS_OPEN topics TOPICS_CLOSEtopics  : topics topic\n                | topictopic : TOPIC_OPEN TEXT TOPIC_CLOSEurl : URL_OPEN URL URL_CLOSEtitle : TITLE_OPEN TEXT TITLE_CLOSErecord_collection : RECORDS_OPEN records RECORDS_CLOSErecords  : records record\n                | recordrecord : RECORD_OPEN idate fdate region numvisits RECORD_CLOSEidate : IDATE_OPEN DATE IDATE_CLOSEfdate : FDATE_OPEN DATE FDATE_CLOSEregion : REGION_OPEN REGION REGION_CLOSEnumvisits : NUMBER_OF_VISITS_OPEN NUMBER_OF_VISITS NUMBER_OF_VISITS_CLOSE'
    
_lr_action_items = {'DATA_OPEN':([0,],[2,]),'$end':([1,10,],[0,-1,]),'TOPICS_OPEN':([2,22,30,],[4,4,-11,]),'SITES_OPEN':([3,14,],[6,-6,]),'TOPIC_OPEN':([4,7,8,15,21,],[9,9,-8,-7,-9,]),'DATA_CLOSE':([5,17,],[10,-2,]),'SITE_OPEN':([6,11,12,18,31,],[13,13,-4,-3,-5,]),'TOPICS_CLOSE':([7,8,15,21,],[14,-8,-7,-9,]),'TEXT':([9,23,],[16,26,]),'SITES_CLOSE':([11,12,18,31,],[17,-4,-3,-5,]),'URL_OPEN':([13,],[20,]),'RECORDS_OPEN':([14,25,],[-6,29,]),'TOPIC_CLOSE':([16,],[21,]),'TITLE_OPEN':([19,27,],[23,-10,]),'URL':([20,],[24,]),'URL_CLOSE':([24,],[27,]),'TITLE_CLOSE':([26,],[30,]),'SITE_CLOSE':([28,35,],[31,-12,]),'RECORD_OPEN':([29,32,33,36,50,],[34,34,-14,-13,-15,]),'RECORDS_CLOSE':([32,33,36,50,],[35,-14,-13,-15,]),'IDATE_OPEN':([34,],[38,]),'FDATE_OPEN':([37,45,],[40,-16,]),'DATE':([38,40,],[41,44,]),'REGION_OPEN':([39,49,],[43,-17,]),'IDATE_CLOSE':([41,],[45,]),'NUMBER_OF_VISITS_OPEN':([42,52,],[47,-18,]),'REGION':([43,],[48,]),'FDATE_CLOSE':([44,],[49,]),'RECORD_CLOSE':([46,53,],[50,-19,]),'NUMBER_OF_VISITS':([47,],[51,]),'REGION_CLOSE':([48,],[52,]),'NUMBER_OF_VISITS_CLOSE':([51,],[53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'data':([0,],[1,]),'topic_collection':([2,22,],[3,25,]),'sites_collection':([3,],[5,]),'topics':([4,],[7,]),'topic':([4,7,],[8,15,]),'sites':([6,],[11,]),'site':([6,11,],[12,18,]),'url':([13,],[19,]),'title':([19,],[22,]),'record_collection':([25,],[28,]),'records':([29,],[32,]),'record':([29,32,],[33,36,]),'idate':([34,],[37,]),'fdate':([37,],[39,]),'region':([39,],[42,]),'numvisits':([42,],[46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> data","S'",1,None,None,None),
  ('data -> DATA_OPEN topic_collection sites_collection DATA_CLOSE','data',4,'p_data','xmlparser.py',18),
  ('sites_collection -> SITES_OPEN sites SITES_CLOSE','sites_collection',3,'p_sites_collection','xmlparser.py',23),
  ('sites -> sites site','sites',2,'p_sites','xmlparser.py',28),
  ('sites -> site','sites',1,'p_sites','xmlparser.py',29),
  ('site -> SITE_OPEN url title topic_collection record_collection SITE_CLOSE','site',6,'p_site','xmlparser.py',34),
  ('topic_collection -> TOPICS_OPEN topics TOPICS_CLOSE','topic_collection',3,'p_topic_collection','xmlparser.py',39),
  ('topics -> topics topic','topics',2,'p_topics','xmlparser.py',44),
  ('topics -> topic','topics',1,'p_topics','xmlparser.py',45),
  ('topic -> TOPIC_OPEN TEXT TOPIC_CLOSE','topic',3,'p_topic','xmlparser.py',50),
  ('url -> URL_OPEN URL URL_CLOSE','url',3,'p_url','xmlparser.py',55),
  ('title -> TITLE_OPEN TEXT TITLE_CLOSE','title',3,'p_title','xmlparser.py',60),
  ('record_collection -> RECORDS_OPEN records RECORDS_CLOSE','record_collection',3,'p_record_collection','xmlparser.py',65),
  ('records -> records record','records',2,'p_records','xmlparser.py',71),
  ('records -> record','records',1,'p_records','xmlparser.py',72),
  ('record -> RECORD_OPEN idate fdate region numvisits RECORD_CLOSE','record',6,'p_record','xmlparser.py',84),
  ('idate -> IDATE_OPEN DATE IDATE_CLOSE','idate',3,'p_idate','xmlparser.py',90),
  ('fdate -> FDATE_OPEN DATE FDATE_CLOSE','fdate',3,'p_fdate','xmlparser.py',96),
  ('region -> REGION_OPEN REGION REGION_CLOSE','region',3,'p_region','xmlparser.py',102),
  ('numvisits -> NUMBER_OF_VISITS_OPEN NUMBER_OF_VISITS NUMBER_OF_VISITS_CLOSE','numvisits',3,'p_numvisits','xmlparser.py',108),
]
