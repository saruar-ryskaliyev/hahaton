import requests, json
from bs4 import BeautifulSoup
def fromLinkToData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text

print(fromLinkToData('https://halykbank.kz/card/dostavka'))