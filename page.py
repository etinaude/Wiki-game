import urllib.request
import pickle
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
        words=""
        for i in links[:-1]:
            if i =="":
                break
            words = words + i+"\n"
        with open("./pages/"+self.title, 'wb') as fp:
            pickle.dump(words, fp)

    def __init__(self, s):
        self.title = s
        self.url = "https://en.wikipedia.org/wiki/"+s
        self.data = urllib.request.urlopen(self.url)
        self.raw = self.data.read()
        self.processed=""
        self.links=[]
        self.process()

