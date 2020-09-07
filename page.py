import urllib.request
import pickle
import re
class Page:
    def process(self):
        links=[]
        wiki_link='\href="/wiki/'
        raw = str(self.raw)
        raw = raw.split("mw-parser-output")[1]
        #print(raw)
        raw = raw.split('id="References"')[0]
        links = re.findall('href="/wiki/\w+"', raw)
        print(links)
        '''try:
            for i in range(1000):
                index= raw.find(wiki_link)+12
                links.append("https://en.wikipedia.org/wiki/"+ raw[index:raw.find("title",index)-2])
                raw = raw[index+1:]
        except:
            pass
        links = links[:links.index("https://en.wikipedia.org/wiki/Main_Page")]
        i=0
        dels = ["File","Special:","International_Standard_Book_Number","Digital_object_identifier","PubMed_Identifier","JSTOR","Help:"]
        while i < len(links):
            for j in dels:
                if j in links[i]:
                    links.remove(links[i])
                    i-=1
                    break
            if "class=" in links[i]:
                links[i] = links[i][:links[i].find("class")]
            if "#" in links[i]:
                links[i] = links[i][:links[i].find("class")]
            if "\"" in links[i]:
                links[i] = links[i][:links[i].find("class")-1]
            i+=1
        '''
        self.links=links
        words=""
        for i in links[:-1]:
            if i =="":
                break
            words = words + i+"\n"
        with open("Page.data", 'wb') as fp:
            pickle.dump(words, fp)

    def __init__(self, s):
        self.url = s
        self.data = urllib.request.urlopen(self.url)
        self.raw = self.data.read()
        self.processed=""
        self.links=""
        self.process()

