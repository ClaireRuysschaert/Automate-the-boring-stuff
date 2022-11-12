import bs4, lxml
from pathlib import Path

exampleFile = open(Path(__file__).parent / 'example.html')

soup = bs4.BeautifulSoup(exampleFile, 'lxml')

author = soup.select('#author')
print(author[0].getText())
author2 = soup.find(attrs={'id':'author'}).text
print(author2)
slogan = soup.select('.slogan')
print(slogan[0].text)
slogan2 = soup.find(attrs={'class':'slogan'})
print(slogan2.text)
link = soup.find('a')
print(link.attrs.get('href'))
# spanElem = soup.select('span')[0]
# print(str(spanElem), spanElem.get('id'), spanElem.attrs)
