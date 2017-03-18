#! usr/bin/python3
# lucky_search.py - opens many search windows

from bs4 import BeautifulSoup
import requests
import sys
import webbrowser

if not len(sys.argv) > 1:
    print('Please Enter Product Keywords')
    print('Usage: amazon_search.py keywords')

print('Shoplifting the product ' + str(' '.join(sys.argv[1:])))

result = requests.get('http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=' + '+'.join(sys.argv[1:]))
result.raise_for_status()

# Retrieve the top search results
soup = BeautifulSoup(result.text, "lxml")

# Open a new browser tab for new result
links = soup.select('.a-link-normal a')
numOpen = len(links)

for i in range(numOpen):
    webbrowser.open('https://amazon.com' + links[i].get('href'))