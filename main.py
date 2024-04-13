from bs4 import BeautifulSoup
import requests

url = 'https://halykbank.kz/cards'
cards = {}
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
