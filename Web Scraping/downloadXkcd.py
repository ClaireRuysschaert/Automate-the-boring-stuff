# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4, lxml

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):

    # Download the page.
    print(f'Downloading the page : {url}')
    requete = requests.get(url)
    requete.raise_for_status()
    soup = bs4.BeautifulSoup(requete.text, 'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print(f'Downloading image ... {comicUrl}')
        res = requests.get(comicUrl)
        res.raise_for_status()
        #the image is saved in res variable

    # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
