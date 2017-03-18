#! usr/bin/python3
# lucky_search.py - opens many search windows

from bs4 import BeautifulSoup
import requests
import sys
import webbrowser

if not len(sys.argv) > 1:
    print('Please Enter Search Keywords')
    print('Usage: lucky_search.py keywords')

print('Googling for ' + str(' '.join(sys.argv[1:])))

result = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
result.raise_for_status()

# Retrieve the top search results
soup = BeautifulSoup(result.text, "lxml")

# Open a new browser tab for new result
links = soup.select('.r a')
numOpen = min(5, len(links))

for i in range(numOpen):
    webbrowser.open('http://google.com' + links[i].get('href'))

