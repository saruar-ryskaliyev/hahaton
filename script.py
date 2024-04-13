import requests, json
import google.generativeai as genai
from bs4 import BeautifulSoup
def fromLinkToData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text
def request(text):
    genai.configure(api_key='AIzaSyBs3c846AoPQ06gmSKt0DtIcswpOp8iwKg')
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content("Give me info about the cashbacks and bonuses for this card. I need you to return me as a json.\n" + text)
    return response.text

text = fromLinkToData('https://halykbank.kz/card/dostavka')
print(request(text))
