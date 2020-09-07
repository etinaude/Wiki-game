import importlib
import urllib.request
import pickle
import re
from page import Page

item = "Harry_Potter"

articles =[]

for i in range(5):
    current = Page(item)
    articles.extend(current.links)
    item = articles[0]
    articles.pop(0)
    print(item)