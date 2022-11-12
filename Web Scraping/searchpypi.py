# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4

#1# Get the command line arg and request the search page
print('Searching...') # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

#2# Find all results
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

div_nulle = soup.select('#xe7COe')
div_nulle.clear()
print(soup)
# Open a browser tab for each result.
linkElems = soup.select('.yuRUbf')

print(linkElems)
numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)
