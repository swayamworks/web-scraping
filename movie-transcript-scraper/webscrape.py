import requests
from bs4 import BeautifulSoup

web = 'https://subslikescript.com'
mov = f'{web}/movies'

response = requests.get(mov)
soup = BeautifulSoup(response.text, "lxml")
box = soup.find('article', class_='main-article')

links = []
for a in box.find_all('a', href=True):
    href = a['href']
    links.append(href)

for link in links:
    try:
        movie_url = f'{web}{link}'
        print(f"Scraping: {movie_url}")

        movie_response = requests.get(movie_url)
        movie_soup = BeautifulSoup(movie_response.text, "lxml")

        article = movie_soup.find('article', class_='main-article')
        title = article.find('h1').get_text()
        transcript = article.find('div', class_='full-script').get_text(strip=True, separator=" ")

        filename = f"{title}.txt".replace(" ", "_").replace("/", "_")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(transcript)
            print(f"Saved: {filename}")

    except AttributeError:
        print(f"Skipped {link} — script or title not found.")
