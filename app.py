#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs
import spacy
import json
import time
import spacy
from spacy.matcher import Matcher
import pandas as pd
import streamlit as st


# In[3]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

st.title('''Get Tickers from News Outlets''')
st.subheader("Choose an option of some of the latest news and get all the tickers from it just in a matter of minutes.")
st.image('pic.png')

url = "https://www.investing.com/rss/news.rss"
path = "C:/Program Files/Google/chromedriver-win64/chromedriver.exe"

service = Service(path)
driver = webdriver.Chrome(service=service)
driver.get(url)
time.sleep(8)
soups = bs(driver.page_source, 'html.parser')

kok = str(soups)
kok1 = kok.split("&")


linklist = []
num = 32
while num in range(len(kok1)):
    x = kok1[num]
    linklist.append(x)
    num += 22
titlelist = []
titlenum = 20
while titlenum in range(len(kok1)):
    y = kok1[titlenum]
    titlelist.append(y)
    titlenum += 22


finallink = []
finaltitle = []


for x in linklist:
    x = x[3:]
    finallink.append(x)
finallink = finallink[:-2]


for x in titlelist:
    x = x[3:]
    finaltitle.append(x)
finaltitle = finaltitle[:-2]


def analyze(url):
    nlp = spacy.blank('en')
    path = "C:/Program Files/Google/chromedriver-win64/chromedriver.exe"
    service = Service(path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    soups = bs(driver.page_source, 'html.parser')
    text1 = soups.select("div.WYSIWYG > p")
    text2 = (str(text1).split("This article"))[0]
    text3 = text2.strip("<p>")
    import re
    CLEANR = re.compile('<.*?>') 
    def cleanhtml(raw_html):
      cleantext = re.sub(CLEANR, '', raw_html)
      return cleantext
    text4 = cleanhtml(text3)
    symbols = pd.read_csv("stocks.csv")['Symbol']
    companies = pd.read_csv("companies.csv")['name_latest'].tolist()
    spacytext = text4
    doc = nlp(spacytext)
    MatcherHits = []
    matcher = Matcher(nlp.vocab)
    pattern = [{"IS_UPPER": True}]
    matcher.add("Stock", [pattern])
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]  # Get string representation
        span = doc[start:end]  # The matched span
        MatcherHits.append(span.text)
    RegHits = []
    import re
    pattern = r"\([^)]*([A-Z]):[^)]*\)"
    matches = re.finditer(pattern, spacytext)
    for match in matches:
        RegHits.append(match.group())
    fin1 = pd.DataFrame({
        "RegEx": RegHits
    })
    fin2 = pd.DataFrame({
        "Matcher": MatcherHits
    })
    st.dataframe(fin1)
    print("Matcher will have a lot of false positives, but it will allow you to get all the tickers that haven't been detected by RegEx.")
    st.dataframe(fin2)

option = st.radio("Select a title:", finaltitle)

if option == finaltitle[0]:
    print("Please wait...")
    analyze(finallink[0])
elif option == finaltitle[1]:
    print("Please wait...")
    analyze(finallink[1])
elif option == finaltitle[2]:
    print("Please wait...")
    analyze(finallink[2])
elif option == finaltitle[3]:
    print("Please wait...")
    analyze(finallink[3])
elif option == finaltitle[4]:
    print("Please wait...")
    analyze(finallink[4])
elif option == finaltitle[5]:
    print("Please wait...")
    analyze(finallink[5])
elif option == finaltitle[6]:
    print("Please wait...")
    analyze(finallink[6])
elif option == finaltitle[7]:
    print("Please wait...")
    analyze(finallink[7])