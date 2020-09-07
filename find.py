import importlib
import urllib.request
import pickle
import re
from page import Page

item = "Harry_Potter"

articles =[]
complete = []
try:
    complete = pickle.load( open( "done", "rb" ) )
except:
    pass

for i in range(20):
    #print(complete)
    current = Page(item)
    articles.extend(current.links)
    while articles[0] in complete:
        articles.pop(0)
    item = articles[0]
    complete.append(item)
    articles.pop(0)
    print(item)
    if (i%5==0):
        print("here")
        pickle.dump( complete, open( "done", "wb" ) )