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
    response = model.generate_content("give me the info in the following format: *name*:*percent of a cashback*\n" + text)
    return response.text

text = fromLinkToData('https://halykbank.kz/index.php/en/card/digital')
print(request(text))


