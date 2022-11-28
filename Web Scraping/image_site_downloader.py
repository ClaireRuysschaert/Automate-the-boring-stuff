# A program that goes to imgur and searches for "fluffy cat"
# Dowloads the first 10 results images 

import os
import bs4
import requests

url = 'https://imgur.com/search?q=fluffy%20cat'
os.makedirs('fluffy cat images', exist_ok=True)

res = requests.get(url) # Download the html page.
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser') # Find the URL of the image.
image_elem = soup.select('.image-list-link')[:10]
for image in image_elem:
    img_src = image.contents[1]
    src_link = img_src.attrs['src']
    image_url = 'https:' + src_link

    res = requests.get(image_url) # Download the image.
    res.raise_for_status()

    #Save the image to the hard drive
    image_file = open(os.path.join('fluffy cat images', os.path.basename(image_url)), 'wb')

    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
