import urllib.request
import json
import re
class Page:
    def process(self):
        links=[]
        wiki_link='\href="/wiki/'
        raw = str(self.raw)
        raw = raw.split('id="mw-content-text"')[1]
        #print(raw)
        raw = raw.split('id="References"')[0]
        links = re.findall('href="/wiki/\w+"', raw)
        for i in range(len(links)):
            links[i]=links[i].replace('href="/wiki/',"")
            links[i]=links[i].replace('"',"")
        self.links=links
        test = json.JSONEncoder().encode({self.title: links})
        with open("json/graph.json", "a") as myfile:
            myfile.write(test[1:-1] +",\n")
            
        

    def __init__(self, s):
        self.title = s
        self.url = "https://en.wikipedia.org/wiki/"+s
        self.data = urllib.request.urlopen(self.url)
        self.raw = self.data.read()
        self.processed=""
        self.links=[]
        self.process()

