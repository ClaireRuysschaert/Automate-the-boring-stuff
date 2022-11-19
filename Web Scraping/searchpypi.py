# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4, lxml

#1# Get the command line arg and request the search page
print('Searching...') # display text while downloading the search result page
url = 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:])
requete = requests.get(url)
requete.raise_for_status()

#2# Find all results
#Retrieve top search result links.
soup = bs4.BeautifulSoup(requete.text, 'lxml')

search_results = soup.find_all(attrs={'class':'package-snippet'})

# Open a browser tab for 5 result.
numOpen = min(5, len(search_results))

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + search_results[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
