This project involves WebScraping using Selenium / BS4, as well as NLP libraries (RegEx, SpaCy, etc.) It acts as follows: The Investment.com RSS gets scraped, giving out links to recent articles and their titles. Having scraped these, the script proceeds to scrape texts from each of these links (stored in the "text4" object). On scraping the text, it removes all HTML tags, and then the whole process eventuates in parsing this text with RegEx and SpaCy Matcher. RegEx is set up to detect the typical pattern of stock mentions on Investment.com. In the event of bad recall, Matcher is also brought to bear. However, Matcher will have bad precision owing to its setup (find all the uppercase words). For the best performance, cognitive effort is required to compare dataframes of RegEx and Matcher so as to define which are False Positives.

WARNING: The 30th row contains the path for your chromedriver.exe, which is preferable due to requests's inability to correctly scrape the data involved. Make sure to have both Google Chrome and its WebDriver installed on your system. You can get the latest version of WebDriver from: https://googlechromelabs.github.io/chrome-for-testing/#stable
Google Chrome can be downloaded from: https://chrome-browser.site/?yclid=5275432894235148287

IMPORTANT: This project is adapted for StreamLit, and thus is supposed to be run exclusively with StreamLit. 

Dependencies:


import requests

from bs4 import BeautifulSoup as bs

import spacy

import json

import time

import spacy

from spacy.matcher import Matcher

import pandas as pd

import streamlit as st

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

import re
