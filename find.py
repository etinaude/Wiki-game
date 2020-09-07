import importlib
import urllib.request
from page import Page
import json

# a very good place to start
item = "ABC"

articles =[]
complete = []
short ={}

try:
    complete = json.load( open("json/done.json", "r" ) )
except:
    pass

for i in range(6152223):
    try:
        current = Page(item)
        articles.extend(current.links)
        short[current.title]= current.links
        while articles[0] in complete:
            articles.pop(0)
        item = articles[0]
        complete.append(item)
        articles.pop(0)
        print(item)
        #print(complete)
        if (i%20==0):
            with open("json/done.json", 'w') as f:
                json.dump(complete, f)
    except Exception as error:
        print(error)
        with open("json/error.json", 'w') as f:
                json.dump(complete, f)