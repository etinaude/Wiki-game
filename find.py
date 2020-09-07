import importlib
import urllib.request
from page import Page
import json

# a very good place to start

articles =[]
complete = []
short ={}
item = "ABC"

try:
    complete = json.load( open("json/done.json", "r" ) )
    item = complete[-1]
except:
    pass

for i in range(6152223):
    try:
        current = Page(item)
        articles.extend(current.links)
        short[current.title]= current.links
        try:
            while articles[0] in complete:
                articles.pop(0)
        except Exception as error:
            print("\terror1:\t",error)
            articles = [complete[-1]]
        item = articles[0]
        complete.append(item)
        articles.pop(0)
        print(item)
        if (i%100==0):
            with open("json/done.json", 'w') as f:
                json.dump(complete, f)
    except Exception as error:
        print("\terror2:\t",error)
        with open("json/done.json", 'w') as f:
               json.dump(complete, f)