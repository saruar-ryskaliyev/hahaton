import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
import json

# URL of the webpage you want to parse
urls = {
    "Eurasian": "https://eubank.kz/list-of-cards/",
    "Jusan": "https://jusan.kz/en/cards",
    "Forte": "https://bank.forte.kz/cards",
    "Halyk": "https://halykbank.kz/cards",
    "BCC": "https://www.bcc.kz/personal/cards/"
}


def find_card_links(url):
    bank_cards = dict()
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the content of the webpage with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags (links) on the webpage
    links = soup.find_all('a')

    # Initialize an empty list to store dictionaries
    link_list = []

    # Loop through each link and extract link text and URL
    for link in links:

        link_text = link.text.strip()  # Extract link text and remove any leading/trailing whitespace
        if 'href' in link.attrs:
            link_url = link['href']  # Extract link URL
            # Create a dictionary with link text and URL
            if 'https://' in link_url:
                link_dict = {'text': link_text, 'url': link_url}

                # Append the dictionary to the link_list
                link_list.append(link_dict)

    links_string = "".join(str(link_list))

    genai.configure(api_key='AIzaSyBs3c846AoPQ06gmSKt0DtIcswpOp8iwKg')

    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    response = model.generate_content(
        links_string + "\nReturn me from this dictionary, links that lead to the information about card, " +
        "return page of each individual card.  Return it like json: Cardname: URL." +
        "Exclude links to pages as 'Debit cards' or 'Credit cards'")
    response_json = json.loads(str(response.text).replace("json", "").replace("`", "").strip())
    #[print(card + " : " + link) for card, link in response_json.items()]
    return response_json


find_card_links(urls["BCC"])
