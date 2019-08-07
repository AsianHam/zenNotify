from lxml import html
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
from requests import Session
import urllib3
import re

toaster = ToastNotifier()

http = urllib3.PoolManager()

payload = {'username': 'abo2114@columbia.edu', 'pass': 'Abmk-2265'}

login = 'https://spsservice.zendesk.com/hc/en-us/signin?return_to=https%3A%2F%2Fspsservice.zendesk.com%2Fhc%2Fen-us&locale=en-us'
url = 'https://spsservice.zendesk.com/agent/filters/114115742371'

def readHtml(link):
    response = http.request('GET', link)
    bSoup = BeautifulSoup(response.data, 'lxml')
    return bSoup

with Session() as s:
    site = s.get(login)
    bsContent = BeautifulSoup(site.content, "html.parser")
    loginData = {"username":"abo2114@columbia.edu", 
                    "password":"Abmk-2265",
                    "csrf_token":"YHJJ6KDWK1pctlc+mg0dzefVqIXePHJWp1gq6+ZbfNgdJOKY5d3jyQKyCT072sNf"}
    s.post(login,loginData)
    homePage = s.get(url)
    print(homePage.content)