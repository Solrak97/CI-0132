class Record:
    def __init__(self, idate, fdate, region, numvisits):
        self.idate = idate
        self.fdate = fdate
        self.region = region
        self.numvisits = numvisits
        pass

    def to_string(self):
        return f'''Idate: {self.idate} | Fdate: {self.fdate} | Region: {self.region} | Numvisits: {self.numvisits}'''



class Site:
    def __init__(self, url, title, topics, records):
        self.url = url
        self.title = title
        self.topics = topics
        self.records = records
        pass

    def to_string(self):
        topics = []
        records = []

        for i in self.topics:
            topics.append(i)

        for i in self.records:
            records.append(i.to_string())
        return f'''Site: 
            URL:            {self.url}
            Title:          {self.title}
            Topics:         {topics:}
            Records:        {records}
        '''
    
class Data:
    def __init__(self, topics, sites):
        self.topics = topics
        self.sites = sites
        pass

    def to_string(self):
        topics = []
        sites = ""

        for i in self.topics:
            topics .append(i)

        for i in self.sites:
            sites += i.to_string() + " "

        return f'''Data:
        Topics: 
        {topics}  
        

        Sites:
        {sites}            
        '''


#   Las listas no son hasheables como tal lo que es un requisito para
#   YACC en t[0], por lo que se crea un wrapper para las listas 
class ListWrapper:
    def __init__(self):
        self.items = []
        pass

    def add_item(self, item):
        self.items.append(item)
        return self
