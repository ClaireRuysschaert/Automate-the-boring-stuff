# web scraper wich find the qualities of Yuki in my website

import bs4, requests, lxml

requete = requests.get("https://claireruysschaert.github.io/")
soup = bs4.BeautifulSoup(requete.text, 'lxml')
# qualities = soup.find_all('li')
qualities = soup.select("li")
for each_quality in qualities:
    print(each_quality.text)
