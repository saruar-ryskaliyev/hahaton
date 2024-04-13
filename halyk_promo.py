import requests
from bs4 import BeautifulSoup

city_ids = {}

url = f"https://halykbank.kz/halykclub/promo"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
links = soup.find_all('a')

# Loop through each link and extract link text and URL
for link in links:
    link_text = link.text.strip()  # Extract link text and remove any leading/trailing whitespace

    # Check if the 'href' attribute exists
    if 'href' in link.attrs:
        link_url = link['href']  # Extract link URL
        if 'city' in link_url:
            city_ids[link_text] = link_url.split("=")[-1]

for city, cid in city_ids.items():
    city_url = f"https://halykbank.kz/halykclub/promo?city={cid}"
    for link in links:
        link_text = link.text.strip()  # Extract link text and remove any leading/trailing whitespace

        # Check if the 'href' attribute exists
        if 'href' in link.attrs and "бонус" in link_text.lower() and "%" in link_text:
            link_url = link['href']  # Extract link URL
            percent = link.text.split()[0]
            if '"' in link_text:
                place = link_text.split('"')[1]
            elif '«' in link_text and '»' in link_text:
                place = link_text[link_text.find("«"):link_text.find("»")+1]
            else:
                place = link_text.split("\n")[0].split(" бонусов в ")[1]
            print(city, percent, place, link_url, sep=" | ")
    print("---------------------")