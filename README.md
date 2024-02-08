This project involves WebScraping using Selenium / BS4, as well as NLP libraries (RegEx, SpaCy, etc.)

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
