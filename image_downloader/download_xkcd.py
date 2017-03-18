#! usr/bin/python3
# download_xkcd.py - A program to download xkcd comics

import requests
import os
from bs4 import BeautifulSoup

url = 'http://xkcd.com'  # base_url
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):

    # Download the image
    result = requests.get(url)
    result.raise_for_status()
    parsed_text = result.text

    # bs object
    soup = BeautifulSoup(parsed_text, "lxml")

    # Finding the url of image
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

        # Download the image (now)
        print('Downloading image %s' % comicUrl)
        img_result = requests.get(comicUrl)
        img_result.raise_for_status()

        # Save the file to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in img_result.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the previous image's URL
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done')

